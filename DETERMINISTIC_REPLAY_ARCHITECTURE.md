# Deterministic Replay Architecture

## Objective

Transform the BHIV Multi-Input Intelligence Platform from an intelligence system into a verifiable intelligence system capable of deterministic reconstruction.

The platform must answer:

* Why was this result produced?
* What evidence created this confidence score?
* Can this exact output be reproduced?
* What changed between evaluations?

---

# Previous Architecture

## Intelligence System

```text
Input
    ↓
Extraction
    ↓
Validation
    ↓
Confidence
    ↓
Evidence
    ↓
Output
```

### Limitation

Outputs could not be reconstructed without re-running:

* OCR
* Extraction
* Validation
* Confidence
* Evidence

This introduced dependency on execution-time behavior.

---

# Current Architecture

## Verifiable Intelligence System

```text
Input
    ↓
Extraction
    ↓
Validation
    ↓
Confidence
    ↓
Evidence
    ↓
Ledger Storage
    ↓
Output
    ↓
Replay Engine
    ↓
Reconstruction
```

---

# Core Components

## Input Layer

Responsible for:

* Request Intake
* File Validation
* Input Validation

Outputs:

* Valid Request

---

## Extraction Layer

Responsible for:

* OCR Processing
* Field Extraction
* Document Understanding

Outputs:

* Structured Identity Data

---

## Validation Layer

Responsible for:

* Field Matching
* Similarity Checks
* Validation Decisions

Outputs:

* Validation Results

---

## Confidence Layer

Responsible for:

* Confidence Scoring
* Confidence Explainability

Outputs:

* Confidence Score
* Reasoning
* Weight Contributions

---

## Evidence Layer

Responsible for:

* Evidence Packaging
* Validation Artifacts
* Trace Information

Outputs:

* Evidence Package

---

## Evidence Ledger

### Purpose

Store replayable execution artifacts.

Location:

```text
ledger/
```

Structure:

```text
ledger/
├── trace1.json
├── trace2.json
├── trace3.json
```

Stored Artifacts:

* Request Snapshot
* Extraction Snapshot
* Validation Snapshot
* Confidence Snapshot
* Evidence Snapshot
* Response Snapshot

---

## Replay Service

### Purpose

Provide deterministic reconstruction.

Input:

```text
trace_id
```

Output:

```json
{
    "trace_id": "...",
    "request": {},
    "extraction": {},
    "validation": {},
    "confidence": {},
    "evidence": {},
    "output": {}
}
```

---

## Replay API

Endpoint:

```http
GET /replay/{trace_id}
```

Purpose:

Allow historical execution reconstruction.

---

# Reconstruction Flow

```text
Trace ID
    ↓
Replay API
    ↓
Replay Service
    ↓
Evidence Ledger
    ↓
Stored Artifacts
    ↓
Reconstructed Execution
```

---

# Deterministic Replay Principle

Replay must never:

* Re-run OCR
* Re-run Extraction
* Re-run Validation
* Re-run Confidence
* Re-run Evidence Generation

Replay only retrieves stored artifacts.

Therefore:

```text
Same Trace ID
=
Same Output
```

---

# Explainable Confidence Flow

```text
Validation Results
    ↓
Confidence Calculation
    ↓
Reasoning Generation
    ↓
Weight Attribution
    ↓
Stored in Ledger
    ↓
Replay Reconstruction
```

Example:

```json
{
    "score": 0.95,
    "reasoning": [
        "Name matched",
        "DOB matched",
        "PAN matched",
        "Aadhaar matched"
    ]
}
```

---

# Evaluation Integration

Deterministic Replay integrates with:

```text
evaluation/
├── dataset.json
├── evaluation_results.json
└── run_evaluation.py
```

Generated Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* False Positive Rate
* False Negative Rate

All metrics are generated from code.

---

# Benefits

## Auditability

Every output can be reconstructed.

---

## Explainability

Every confidence score can be explained.

---

## Reproducibility

Replay returns identical outputs.

---

## Traceability

Every output is linked to a trace_id.

---

## Evidence-Based Decisions

Outputs are backed by stored evidence artifacts.

---

# Acceptance Criteria Mapping

| Requirement               | Status |
| ------------------------- | ------ |
| Replay Engine             | PASS   |
| Evidence Ledger           | PASS   |
| Confidence Explainability | PASS   |
| Replay API                | PASS   |
| Deterministic Replay      | PASS   |
| Evaluation Framework      | PASS   |
| Reproducible Metrics      | PASS   |

---

# Final State

The BHIV Multi-Input Intelligence Platform has evolved from a reusable intelligence capability into a verifiable intelligence capability that supports deterministic replay, evidence-backed reconstruction, confidence explainability, and reproducible evaluation.
