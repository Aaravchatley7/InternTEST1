# Failure Classification Report

## OCR Failures

Examples:

- Blurry Images
- Cropped Documents
- Poor Lighting

Mitigation:

- Preprocessing
- OCR Fallback

---

## Extraction Failures

Examples:

- Missing Aadhaar Number
- Missing PAN Number

Mitigation:

- Regex Fallback
- LLM Extraction

---

## Validation Failures

Examples:

- User Data Mismatch
- OCR Errors

Mitigation:

- Normalization
- Fuzzy Matching

---

## Replay Failures

Examples:

- Missing Trace ID
- Missing Ledger Artifact

Mitigation:

- Error Handling

---

## RAG Failures

Examples:

- Weak Context
- Missing Source Data

Mitigation:

- Better Retrieval
- Larger Datasets