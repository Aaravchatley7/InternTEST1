"""
langgraph_flow.py — Document verification orchestration pipeline.

Steps:
  1. OCR each uploaded document image
  2. Extract structured fields with regex + optional LLM
  3. Compare extracted fields against user-submitted form data
  4. Send result email
  5. Return result dict to Flask for UI rendering
"""

from ocr_utils import extract_text
from llm_utils import extract_fields_from_text
from compare_utils import compare_fields
from email_utils import send_email, build_verification_email


def _doc_type_from_path(path: str) -> str:
    p = path.lower()
    if 'pan' in p:
        return 'pan'
    if 'passport' in p:
        return 'passport'
    return 'aadhaar'


def run_langgraph_workflow(form_data: dict, document_paths: dict) -> dict:
    """
    Run the full verification pipeline.

    Args:
        form_data: dict with keys name, phone, email, dob, aadhaar_number, pan_number
        document_paths: dict with optional keys aadhaar_image, pan_image, passport_image

    Returns:
        result dict with keys: match, fields, extracted, email_sent, ocr_texts
    """
    aadhaar_ext  = {}
    pan_ext      = {}
    passport_ext = {}
    ocr_texts    = {}

    # ── OCR + field extraction per document ────────────────────────────────────
    for key, doc_type in [
        ('aadhaar_image',  'aadhaar'),
        ('pan_image',      'pan'),
        ('passport_image', 'passport'),
    ]:
        path = document_paths.get(key)
        if not path:
            continue

        print(f"[WORKFLOW] Processing {doc_type}: {path}")
        text = extract_text(path)
        ocr_texts[doc_type] = text

        if not text.strip():
            print(f"[WORKFLOW] OCR returned empty for {doc_type}")
            continue

        extracted = extract_fields_from_text(text, doc_type)
        print(f"[WORKFLOW] {doc_type} extracted: {extracted}")

        if doc_type == 'aadhaar':
            aadhaar_ext = extracted
        elif doc_type == 'pan':
            pan_ext = extracted
        elif doc_type == 'passport':
            passport_ext = extracted

    # ── Compare ────────────────────────────────────────────────────────────────
    result = compare_fields(form_data, aadhaar_ext, pan_ext, passport_ext)
    result['ocr_texts'] = ocr_texts
    print(f"[WORKFLOW] Verdict: {'PASS' if result['match'] else 'FAIL'}")
    print(f"[WORKFLOW] Fields: {result['fields']}")

    # ── Email ──────────────────────────────────────────────────────────────────
    try:
        body_text, body_html = build_verification_email(form_data, result)
        subject = (
            "✅ Verification Successful — DocVerify"
            if result['match'] else
            "❌ Verification Failed — DocVerify"
        )
        email_sent = send_email(form_data['email'], subject, body_text, body_html)
    except Exception as e:
        print(f"[WORKFLOW] Email error: {e}")
        email_sent = False

    result['email_sent'] = email_sent
    return result
