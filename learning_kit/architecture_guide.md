# BHIV Architecture Guide

## Overview

The BHIV Multi-Input Intelligence Platform is a reusable intelligence capability for document processing, validation, confidence scoring, evidence generation, observability, provenance, replay, and retrieval-augmented generation (RAG).

The platform is designed to be modular, extensible, replayable, and reusable across multiple BHIV products.

---

# High-Level Architecture

```text
User Input
    ↓
Input Layer
    ↓
Extraction Layer
    ↓
Validation Layer
    ↓
Confidence Layer
    ↓
Evidence Layer
    ↓
Observability Layer
    ↓
Provenance Layer
    ↓
Evidence Ledger
    ↓
Replay Engine
```

---

# Layer-by-Layer Explanation

## Input Layer

Purpose:

- Validate incoming requests
- Validate uploaded files
- Enforce request requirements

Location:

```text
layers/input_layer.py
```

Outputs:

- Validated Request

---

## Extraction Layer

Purpose:

- OCR Processing
- Field Extraction
- Identity Understanding

Location:

```text
layers/extraction_layer.py
services/ocr_service.py
services/llm_service.py
```

Outputs:

- Name
- DOB
- Aadhaar Number
- PAN Number
- Other Identity Fields

---

## Validation Layer

Purpose:

Compare extracted document information with user-provided information.

Location:

```text
layers/validation_layer.py
```

Outputs:

- Field Match Results
- Validation Decisions

---

## Confidence Layer

Purpose:

Generate explainable confidence scores.

Location:

```text
layers/confidence_layer.py
```

Outputs:

- Confidence Score
- Confidence Level
- Confidence Reasoning
- Weight Contributions

---

## Evidence Layer

Purpose:

Generate evidence-backed validation artifacts.

Location:

```text
layers/evidence_layer.py
```

Outputs:

- Evidence Package
- Validation Artifacts

---

## Observability Layer

Purpose:

Track platform behavior.

Location:

```text
layers/observability_layer.py
```

Capabilities:

- Logging
- Metrics
- Health Monitoring
- Trace IDs

---

## Provenance Layer

Purpose:

Track lineage and origin of outputs.

Location:

```text
services/provenance_service.py
```

Outputs:

- Trace Metadata
- Contract Metadata
- Source Metadata

---

## Evidence Ledger

Purpose:

Store replayable execution artifacts.

Location:

```text
ledger/
```

Stores:

- Request Snapshot
- Extraction Snapshot
- Validation Snapshot
- Confidence Snapshot
- Evidence Snapshot
- Response Snapshot

---

## Replay Engine

Purpose:

Reconstruct historical executions.

Location:

```text
services/replay_service.py
```

Inputs:

- trace_id

Outputs:

- Reconstructed Execution

---

# Design Principles

The platform follows the following principles:

- Modularity
- Reusability
- Explainability
- Observability
- Traceability
- Replayability
- Extensibility

---

# Extension Model

Future document types can be added using:

```text
capabilities/
```

Examples:

- Passport
- Driving Licence
- Voter ID
- Certificates
- Invoices
- Government Forms

---

# Capability SDK

The platform exposes reusable interfaces through:

```text
sdk/
```

Examples:

```python
from sdk.verification_sdk import VerificationSDK

sdk = VerificationSDK()

result = sdk.verify(
    form_data,
    document_path,
    document_type
)
```

---

# Conclusion

The BHIV Multi-Input Intelligence Platform is designed as a reusable ecosystem capability that combines document intelligence, validation, confidence scoring, evidence generation, replayability, and knowledge retrieval into a single extensible architecture.