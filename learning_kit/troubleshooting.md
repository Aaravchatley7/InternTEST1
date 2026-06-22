# Troubleshooting Guide

## OCR Failures

### Symptoms

- Aadhaar number missing
- PAN number missing
- Incorrect OCR text
- Empty extraction

### Causes

- Blurry image
- Cropped image
- Poor lighting
- Low resolution

### Fixes

- Upload clearer image
- Increase image resolution
- Verify OCR preprocessing

### Files

```text
services/ocr_service.py
layers/extraction_layer.py
```

---

## OpenRouter Failures

### Symptoms

- Empty extraction
- API errors
- Timeout errors

### Causes

- Missing API key
- Network issue
- API rate limit

### Fixes

Verify:

```env
OPENROUTER_API_KEY
```

Check:

- Internet connection
- API key validity

### Files

```text
services/llm_service.py
```

---

## Validation Failures

### Symptoms

- Expected match returns false
- Incorrect validation results

### Causes

- OCR noise
- Formatting differences
- Data normalization issues

### Fixes

Review:

- Validation rules
- Comparison logic
- Normalization logic

### Files

```text
layers/validation_layer.py
services/comparison_service.py
```

---

## Replay Failures

### Symptoms

- Trace ID not found
- Replay returns not_found

### Causes

- Missing ledger artifact
- Invalid trace ID

### Fixes

Verify:

```text
ledger/
```

Check:

- Trace ID exists
- Ledger file exists

### Files

```text
services/replay_service.py
services/evidence_ledger.py
```

---

## RAG Failures

### Symptoms

- Poor answers
- Missing context
- Empty responses

### Causes

- PDF not uploaded
- Empty vector store
- Weak retrieval

### Fixes

Verify:

```text
vectorstore/
```

Re-upload document.

### Files

```text
services/rag_service.py
services/vector_builder.py
layers/rag_layer.py
```

---

## Metrics Failures

### Symptoms

- Metrics not updating
- Incorrect counts

### Causes

- Metrics file missing
- Update function not called

### Fixes

Verify:

```text
metrics/metrics.json
```

### Files

```text
layers/observability_layer.py
```

---

## Health Endpoint Failures

### Symptoms

- Health status degraded

### Causes

- Missing folders
- Missing metrics
- Missing ledger

### Fixes

Verify:

```text
ledger/
metrics/
uploads/
vectorstore/
```

---

## Deployment Failures

### Symptoms

- Uvicorn startup failure
- Import errors
- Missing modules

### Fixes

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app:app --reload
```

Verify:

- Python Version
- Environment Variables
- Project Structure

---

## Test Failures

### Symptoms

- Pytest failures

### Fixes

Run:

```bash
pytest
```

Review:

- Error Message
- Failed Module
- Missing Dependency

---

# Diagnostic Checklist

Before reporting an issue:

✓ Application Starts

✓ API Key Configured

✓ Metrics Available

✓ Ledger Available

✓ Tests Pass

✓ Vector Store Exists

✓ Required Folders Exist

---

# Escalation Path

1. Check Logs
2. Check Metrics
3. Check Trace ID
4. Check Replay Output
5. Review Validation Evidence
6. Reproduce Issue
7. Document Findings