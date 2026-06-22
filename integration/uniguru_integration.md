# UniGuru Integration Guide

## Purpose

Enable UniGuru to consume BHIV verification and document intelligence capabilities.

---

# Use Cases

- Student Identity Verification
- Scholarship Verification
- Admission Document Validation
- Educational Certificate Processing

---

# Integration Model

API Linked

```text
UniGuru
    ↓
BHIV Verification API
    ↓
Validation Result
```

---

# Inputs

- Student Documents
- Identity Information

---

# Outputs

- Validation Results
- Confidence Scores
- Evidence Packages

---

# Recommended APIs

POST /documents/verify

GET /replay/{trace_id}

GET /health

GET /metrics