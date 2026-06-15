# Failure Analysis Report

## Objective

Identify and categorize observed failures during evaluation.

---

# OCR Failures

## Causes

* Blurry Images
* Low Resolution
* Poor Lighting
* Skewed Documents

Mitigations:

* OCR Preprocessing
* EasyOCR
* Tesseract Fallback

---

# Extraction Failures

## Causes

* OCR Character Errors
* Missing Fields
* Formatting Variations

Mitigations:

* Regex Recovery
* Field Fusion
* LLM Extraction

---

# Validation Failures

## Causes

* User Data Mismatch
* Typographical Errors

Mitigations:

* Fuzzy Matching
* Normalization

---

# RAG Failures

## Causes

* Missing Context
* Poor Source Material

Mitigations:

* Similarity Search
* Context Filtering

---

# Deployment Failures

## Causes

* Missing Environment Variables
* Missing Vector Store
* Missing Uploaded Documents

Mitigations:

* Deployment Documentation
* Environment Validation

---

# LLM Failures

## Causes

* Hallucination
* Missing Context
* Incomplete OCR

Mitigations:

* Evidence Layer
* Confidence Layer
* Fallback Recovery

---

# Conclusion

Observed failures are understood, categorized, and mitigated through layered system design.
