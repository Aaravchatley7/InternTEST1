"""
compare_utils.py — Normalize and compare form fields against extracted document fields.

Name matching handles:
  - Fused OCR output (PRIYAMEHTA == PRIYA MEHTA)
  - Word-set overlap ≥75% for middle-name differences
  - Substring matching for first-name-only entries

Overall pass/fail logic:
  - Name MUST match.
  - If the user submitted an Aadhaar/PAN number, at least one must match.
  - DOB and phone are informational (shown but don't block pass).
"""

import re


# ─────────────────────────────────────────────────────────────────────────────
# Normalizers
# ─────────────────────────────────────────────────────────────────────────────

def _alpha_only(s: str) -> str:
    """Letters only, uppercase, no spaces — for space-insensitive name compare."""
    return re.sub(r'[^A-Z]', '', (s or '').upper())


def _clean_name(s: str) -> str:
    """Uppercase, letters + spaces only, collapsed whitespace."""
    return re.sub(r'\s+', ' ', re.sub(r'[^A-Za-z\s]', '', s or '').strip().upper())


def _norm_dob(dob: str) -> str:
    """Normalize any date format to DD/MM/YYYY."""
    if not dob:
        return ''
    dob = str(dob).strip()
    # YYYY-MM-DD or YYYY/MM/DD
    m = re.match(r'^(\d{4})[-/.](\d{1,2})[-/.](\d{1,2})$', dob)
    if m:
        return f"{int(m.group(3)):02d}/{int(m.group(2)):02d}/{m.group(1)}"
    # DD-MM-YYYY or DD/MM/YYYY or DD.MM.YYYY
    m = re.match(r'^(\d{1,2})[-/.](\d{1,2})[-/.](\d{2,4})$', dob)
    if m:
        yr = m.group(3)
        if len(yr) == 2:
            yr = ('20' if int(yr) <= 30 else '19') + yr
        return f"{int(m.group(1)):02d}/{int(m.group(2)):02d}/{yr}"
    return dob


def _norm_aadhaar(n: str) -> str:
    return re.sub(r'[\s\-]', '', str(n or ''))


def _norm_pan(n: str) -> str:
    return str(n or '').strip().upper()


def _norm_phone(n: str) -> str:
    digits = re.sub(r'\D', '', str(n or ''))
    return digits[-10:] if len(digits) >= 10 else digits


# ─────────────────────────────────────────────────────────────────────────────
# Name matching
# ─────────────────────────────────────────────────────────────────────────────

def _name_match(form: str, doc: str) -> bool:
    """
    True if form_name matches doc_name using three strategies:
      1. Exact after normalization
      2. Space-insensitive (handles fused OCR: PRIYAMEHTA == PRIYA MEHTA)
      3. Word-set overlap ≥ 75%
    """
    f = _clean_name(form)
    d = _clean_name(doc)
    if not f or not d:
        return False

    # 1. Exact
    if f == d:
        return True

    # 2. Space-insensitive (fused OCR fix)
    if _alpha_only(f) == _alpha_only(d):
        return True

    # 3. One is a prefix/suffix of the other (first-name-only cases)
    fa, da = _alpha_only(f), _alpha_only(d)
    if fa and da and (fa in da or da in fa):
        return True

    # 4. Word-set overlap
    f_words = set(f.split())
    d_words = set(d.split())
    if f_words and d_words:
        overlap = len(f_words & d_words) / len(f_words)
        if overlap >= 0.75:
            return True

    return False


# ─────────────────────────────────────────────────────────────────────────────
# Public API
# ─────────────────────────────────────────────────────────────────────────────

def compare_fields(form_data: dict,
                   aadhaar_ext: dict,
                   pan_ext: dict,
                   passport_ext: dict | None = None) -> dict:
    """
    Compare user-submitted form data against OCR-extracted document fields.

    Returns a result dict:
    {
        "match": bool,
        "fields": {
            "name":    {"match": bool, "form_value": str, "doc_value": str},
            "dob":     {...},
            "aadhaar": {...},
            "pan":     {...},
            "phone":   {...},
        },
        "extracted": {"aadhaar": dict, "pan": dict, "passport": dict}
    }
    """
    a  = aadhaar_ext  or {}
    p  = pan_ext      or {}
    pp = passport_ext or {}
    fields = {}

    # ── NAME ──────────────────────────────────────────────────────────────────
    form_name = _clean_name(form_data.get('name', ''))
    # Collect all names from all documents
    doc_name_candidates = [
        a.get('name', ''), p.get('name', ''), pp.get('name', '')
    ]
    nm = any(_name_match(form_name, dn) for dn in doc_name_candidates)
    best_doc_name = _clean_name(next((n for n in doc_name_candidates if n), ''))
    fields['name'] = {
        'match':      nm,
        'form_value': form_name     or '—',
        'doc_value':  best_doc_name or 'Not extracted',
    }

    # ── DOB ───────────────────────────────────────────────────────────────────
    form_dob = _norm_dob(form_data.get('dob', ''))
    doc_dobs  = [_norm_dob(a.get('dob','')),
                 _norm_dob(p.get('dob','')),
                 _norm_dob(pp.get('dob',''))]
    dob_match = bool(form_dob and any(d == form_dob for d in doc_dobs if d))
    best_doc_dob = next((d for d in doc_dobs if d), 'Not extracted')
    fields['dob'] = {
        'match':      dob_match,
        'form_value': form_dob      or 'Not provided',
        'doc_value':  best_doc_dob,
    }

    # ── AADHAAR ───────────────────────────────────────────────────────────────
    form_aadhaar = _norm_aadhaar(form_data.get('aadhaar_number', ''))
    doc_aadhaar  = _norm_aadhaar(
        a.get('aadhaar_number', '') or pp.get('aadhaar_number', '')
    )
    aadhaar_match = bool(form_aadhaar and doc_aadhaar and form_aadhaar == doc_aadhaar)
    fields['aadhaar'] = {
        'match':      aadhaar_match,
        'form_value': form_aadhaar or 'Not provided',
        'doc_value':  doc_aadhaar  or 'Not extracted',
    }

    # ── PAN ───────────────────────────────────────────────────────────────────
    form_pan = _norm_pan(form_data.get('pan_number', ''))
    doc_pan  = _norm_pan(p.get('pan_number', '') or pp.get('pan_number', ''))
    pan_match = bool(form_pan and doc_pan and form_pan == doc_pan)
    fields['pan'] = {
        'match':      pan_match,
        'form_value': form_pan or 'Not provided',
        'doc_value':  doc_pan  or 'Not extracted',
    }

    # ── PHONE ─────────────────────────────────────────────────────────────────
    form_phone = _norm_phone(form_data.get('phone', ''))
    doc_phones = [
        _norm_phone(a.get('phone','')),
        _norm_phone(p.get('phone','')),
        _norm_phone(pp.get('phone','')),
    ]
    ph_match = bool(form_phone and any(
        dp and form_phone == dp for dp in doc_phones
    ))
    best_doc_phone = next((dp for dp in doc_phones if dp), 'Not in document')
    fields['phone'] = {
        'match':      ph_match,
        'form_value': form_phone    or '—',
        'doc_value':  best_doc_phone,
    }

    # ── OVERALL VERDICT ────────────────────────────────────────────────────────
    # Name must match.
    # If user provided an ID number, at least one must match the document.
    id_provided = bool(form_aadhaar or form_pan)
    id_ok       = aadhaar_match or pan_match
    overall     = nm and (id_ok if id_provided else True)

    return {
        'match':     overall,
        'fields':    fields,
        'extracted': {'aadhaar': a, 'pan': p, 'passport': pp},
    }
