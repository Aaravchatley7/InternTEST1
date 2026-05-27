"""
llm_utils.py — Extract structured fields from OCR text.

Tier 1 (always runs, no API): Smart regex tuned for Aadhaar / PAN / Passport layouts.
Tier 2 (runs when Tier 1 is incomplete): OpenRouter free-tier LLM
  - Models tried in order: mistral-7b-instruct:free, llama-3.2-3b-instruct:free
  - No credit card required — sign up at https://openrouter.ai

Set OPENROUTER_API_KEY in config.py or as an env var.
"""

import re
import os
import json
import requests

try:
    from config import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = ""

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", OPENROUTER_API_KEY)

_FREE_MODELS = [
    "mistralai/mistral-7b-instruct:free",
    "meta-llama/llama-3.2-3b-instruct:free",
    "google/gemma-3-1b-it:free",
]

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

_SKIP = {
    'GOVERNMENT','GOVERNMENTOF','INDIA','AADHAAR','INCOME','TAX','DEPARTMENT',
    'PERMANENT','ACCOUNT','NUMBER','MALE','FEMALE','GENDER','DATE','BIRTH',
    'VALID','PASSPORT','REPUBLIC','NATIONALITY','DOB','OF','THE','AND','FOR',
    'UNIQUE','IDENTIFICATION','AUTHORITY','UIDAI','PAN','CARD','VOTER',
    'PHOTO','ADDRESS','ELECTORAL','FATHER','MOTHER','SIGNATURE','GOVT',
    'FON','BHARAT','SARKAR','ELECTORAL',
}

_HEADER_RE = re.compile(
    r'(government|india|aadhaar|unique|authority|uidai|income|tax|permanent'
    r'|account|भारत|sarkar|republic|passport|voter|electoral|pan\s*card'
    r'|department|identification)',
    re.IGNORECASE
)

_SKIP_PREFIX_RE = re.compile(
    r'^\s*(S\s*/?O|D\s*/?O|W\s*/?O|Father|Mother|Address|Addr|VID|DOB|Date'
    r'|Gender|Phone|Mobile|PHOTO|Signature|Village|Post|District|State|Pin)',
    re.IGNORECASE
)


# ─────────────────────────────────────────────────────────────────────────────
# Tier 1: Regex / heuristic extraction
# ─────────────────────────────────────────────────────────────────────────────

def _is_name_line(line: str) -> bool:
    """Return True if line looks like a person's name."""
    if _HEADER_RE.search(line):
        return False
    if _SKIP_PREFIX_RE.match(line):
        return False
    # Must have enough alpha chars
    alpha = re.sub(r'[^A-Za-z]', '', line)
    if len(alpha) < 3:
        return False
    # Reject lines heavy with digits
    if len(re.findall(r'\d', line)) > 2:
        return False
    clean = re.sub(r'[^A-Za-z\s]', '', line).strip().upper()
    words = [w for w in clean.split() if len(w) >= 2 and w not in _SKIP]
    if not (1 <= len(words) <= 5):
        return False
    # At least one word must contain a vowel (names do)
    return any(re.search(r'[AEIOU]', w) for w in words)


def _extract_name(lines: list) -> str | None:
    # Pass 1: explicit label
    for line in lines:
        m = re.match(r'^(?:Name|NAME)\s*[:\-]?\s*(.+)$', line, re.IGNORECASE)
        if m:
            candidate = re.sub(r'[^A-Za-z\s]', '', m.group(1)).strip().upper()
            words = [w for w in candidate.split() if w not in _SKIP and len(w) >= 2]
            if 1 <= len(words) <= 5:
                return ' '.join(words)
    # Pass 2: first line that looks like a name
    for line in lines:
        if _is_name_line(line):
            clean = re.sub(r'[^A-Za-z\s]', '', line).strip().upper()
            words = [w for w in clean.split() if len(w) >= 2 and w not in _SKIP]
            if words:
                return ' '.join(words)
    return None


def _extract_dob(text: str) -> str | None:
    patterns = [
        r'(?:DOB|D\.O\.B|Date\s*of\s*Birth|Born|YOB|Birth\s*Date)\s*[:\-]?\s*(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})',
        r'(?:DOB|D\.O\.B|Date\s*of\s*Birth|Born)\s*[:\-]?\s*(\d{4}[\/\-\.]\d{2}[\/\-\.]\d{2})',
        r'\b(\d{2}[\/\-]\d{2}[\/\-]\d{4})\b',
        r'\b(\d{4}[\/\-]\d{2}[\/\-]\d{2})\b',
        r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\b',
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return m.group(1).strip().replace('-', '/').replace('.', '/')
    return None


def _extract_aadhaar(text: str) -> str | None:
    """
    Find the 12-digit Aadhaar number.
    Strategy: remove VID (16-digit) sequences first, then find last 12-digit group.
    VID format: 4 groups of 4 digits = 16 digits total.
    Aadhaar format: 3 groups of 4 digits = 12 digits total.
    """
    # Remove VID line entirely
    clean = re.sub(r'(?i)\bVID\b[^\n]*', '', text)
    # Remove standalone 16-digit groups (4-4-4-4)
    clean = re.sub(r'(?<!\d)\d{4}[\s]?\d{4}[\s]?\d{4}[\s]?\d{4}(?!\d)', '', clean)

    matches = list(re.finditer(r'(?<!\d)(\d{4}[\s]?\d{4}[\s]?\d{4})(?!\d)', clean))
    if matches:
        return re.sub(r'\s', '', matches[-1].group(1))

    # Fallback: last 12-digit group in original text
    matches = list(re.finditer(r'(?<!\d)(\d{4}[\s]?\d{4}[\s]?\d{4})(?!\d)', text))
    return re.sub(r'\s', '', matches[-1].group(1)) if matches else None


def _extract_pan(text: str) -> str | None:
    m = re.search(r'\b([A-Z]{5}[0-9]{4}[A-Z])\b', text.upper())
    return m.group(1) if m else None


def _extract_passport_num(text: str) -> str | None:
    m = re.search(r'\b([A-Z]\d{7})\b', text.upper())
    return m.group(1) if m else None


def _regex_extract(text: str, doc_type: str) -> dict:
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    oneline = ' '.join(lines)
    result = {}

    name = _extract_name(lines)
    if name:
        result['name'] = name

    dob = _extract_dob(oneline)
    if dob:
        result['dob'] = dob

    if doc_type in ('aadhaar', 'unknown'):
        # Pass original multiline text so VID line removal works correctly
        num = _extract_aadhaar(text)
        if num:
            result['aadhaar_number'] = num

    if doc_type in ('pan', 'unknown'):
        pan = _extract_pan(oneline)
        if pan:
            result['pan_number'] = pan
        fn = re.search(
            r"(?:Father'?s?\s*Name|Father|S/?O|Son\s*of|D/?O|Daughter\s*of)"
            r"\s*[:\-]?\s*([A-Za-z][A-Za-z\s]{2,35}?)(?=\s*(?:Date|DOB|Gender|Address|Phone|$|\n))",
            text, re.IGNORECASE
        )
        if fn:
            result['father_name'] = re.sub(r'[^A-Za-z\s]', '', fn.group(1)).strip().upper()

    if doc_type in ('passport', 'unknown'):
        pp = _extract_passport_num(oneline)
        if pp:
            result['passport_number'] = pp

    m = re.search(r'\b(MALE|FEMALE|TRANSGENDER)\b', oneline.upper())
    if m:
        result['gender'] = m.group(1)

    m = re.search(r'(?<!\d)(\+?91[\s\-]?)?([6-9]\d{9})(?!\d)', oneline)
    if m:
        result['phone'] = re.sub(r'[\s\-\+]', '', m.group(0))

    return result


# ─────────────────────────────────────────────────────────────────────────────
# Tier 2: OpenRouter free LLM
# ─────────────────────────────────────────────────────────────────────────────

def _openrouter_extract(text: str, doc_type: str) -> dict:
    if not OPENROUTER_API_KEY:
        return {}

    prompt = (
        f"You are an expert OCR parser for Indian identity documents.\n"
        f"Extract fields from this {doc_type.upper()} card OCR text:\n\n"
        f'"""\n{text}\n"""\n\n'
        f"Return ONLY a valid JSON object with these keys (null if not found):\n"
        f"- name: full name in UPPERCASE (string)\n"
        f"- dob: date of birth as DD/MM/YYYY (string)\n"
        f"- aadhaar_number: exactly 12 digits no spaces (string or null)\n"
        f"- pan_number: exactly 10 chars uppercase like ABCDE1234F (string or null)\n"
        f"- gender: MALE or FEMALE or TRANSGENDER (string or null)\n"
        f"- phone: 10-digit Indian mobile number (string or null)\n"
        f"- passport_number: format A1234567 (string or null)\n\n"
        f"IMPORTANT: Return raw JSON only. No markdown, no explanation, no backticks."
    )

    for model in _FREE_MODELS:
        try:
            resp = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://docverify.app",
                    "X-Title": "DocVerify",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.0,
                    "max_tokens": 350,
                },
                timeout=25,
            )

            if resp.status_code != 200:
                print(f"[LLM] {model} HTTP {resp.status_code}: {resp.text[:120]}")
                continue

            raw = resp.json()["choices"][0]["message"]["content"].strip()
            print(f"[LLM] {model} → {raw[:200]}")

            # Strip markdown fences
            raw = re.sub(r'^```(?:json)?\s*', '', raw, flags=re.MULTILINE)
            raw = re.sub(r'\s*```$', '', raw, flags=re.MULTILINE).strip()

            # Extract JSON object
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            if m:
                parsed = json.loads(m.group(0))
                # Clean up null strings
                return {k: v for k, v in parsed.items() if v and v != 'null'}

        except json.JSONDecodeError as e:
            print(f"[LLM] JSON parse error ({model}): {e}")
        except Exception as e:
            print(f"[LLM] Error ({model}): {e}")

    return {}


# ─────────────────────────────────────────────────────────────────────────────
# Public API
# ─────────────────────────────────────────────────────────────────────────────

def extract_fields_from_text(text: str, doc_type: str) -> dict:
    """
    Extract structured fields from OCR text.
    Regex (Tier 1) always runs. OpenRouter (Tier 2) fills gaps when key fields missing.
    """
    result = _regex_extract(text, doc_type)
    print(f"[EXTRACT] Tier-1 regex: {result}")

    has_name = bool(result.get('name'))
    has_dob  = bool(result.get('dob'))
    has_id   = bool(
        result.get('aadhaar_number') or
        result.get('pan_number') or
        result.get('passport_number')
    )

    if not (has_name and has_dob and has_id) and OPENROUTER_API_KEY:
        print(f"[EXTRACT] Incomplete (name={has_name}, dob={has_dob}, id={has_id}) → calling LLM")
        llm = _openrouter_extract(text, doc_type)
        for k, v in llm.items():
            if v and not result.get(k):
                result[k] = str(v)
        print(f"[EXTRACT] After LLM merge: {result}")
    elif not OPENROUTER_API_KEY:
        print("[EXTRACT] No OPENROUTER_API_KEY set — regex-only mode")

    print(f"[EXTRACT] Final: {result}")
    return result
