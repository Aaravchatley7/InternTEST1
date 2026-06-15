# Capability Authority Matrix

## Purpose

Define the authority boundaries of the BHIV Multi-Input Intelligence Platform to prevent capability drift and authority misinterpretation.

---

# Authority Owned

The platform owns the following responsibilities.

## Extraction Authority

Responsible For:

* OCR Extraction
* Document Field Detection
* Structured Data Extraction
* Retrieval Context Extraction

Outputs:

* Extracted Fields
* OCR Results
* Retrieved Context

---

## Validation Authority

Responsible For:

* Identity Validation
* Field Comparison
* Similarity Matching
* Match Determination

Outputs:

* Validation Result
* Validation Score

---

## Confidence Authority

Responsible For:

* Confidence Estimation
* Confidence Scoring
* Confidence Categorization

Outputs:

* Confidence Score
* Confidence Level

---

## Evidence Authority

Responsible For:

* Evidence Generation
* Verification Traceability
* Supporting Artifacts

Outputs:

* Evidence Package

---

## Observability Authority

Responsible For:

* Metrics
* Trace IDs
* Logging
* Latency Monitoring

Outputs:

* Observability Metadata

---

# Authority Explicitly NOT Owned

The platform does NOT own the following responsibilities.

## Governance Authority

Not Responsible For:

* Policy Decisions
* Compliance Decisions
* Regulatory Interpretation

---

## Execution Authorization

Not Responsible For:

* User Authorization
* Approval Decisions
* Operational Actions

---

## Truth Ownership

Not Responsible For:

* Declaring Ground Truth
* Legal Identity Determination
* Official Certification

---

## Human Decision Making

Not Responsible For:

* Final Human Decisions
* Governance Reviews
* Administrative Actions

---

# Upstream Dependencies

* EasyOCR
* Tesseract
* OpenRouter
* FAISS
* LangChain
* User Submitted Documents

---

# Downstream Consumers

* UniGuru
* Parikshak
* Signals Corps
* Verification Systems
* Knowledge Platforms
* Document Intelligence Systems

---

# Authority Ceiling

The capability may provide:

* Extraction
* Validation
* Confidence
* Evidence

The capability may NOT provide:

* Governance
* Legal Authority
* Approval Authority
* Policy Authority

---

# Conclusion

Confidence scores are estimates.

Validation scores are assessments.

Neither should be interpreted as governance authority or truth ownership.
