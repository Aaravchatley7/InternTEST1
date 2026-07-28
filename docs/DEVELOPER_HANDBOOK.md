# Developer Handbook

## BHIV Multi-Input Document Intelligence Platform

Version: 1.0.0

Status: Engineering Handover

---

# Purpose

This handbook enables a new engineer to understand, operate, debug, extend, and maintain the BHIV Multi-Input Document Intelligence Platform without prior project knowledge.

The platform is designed as a modular document intelligence capability centered around document verification, explainable confidence scoring, deterministic replay, and Retrieval-Augmented Generation (RAG).

---

# What Does This System Do?

The platform processes identity documents, extracts structured information using OCR and LLM-assisted extraction, validates extracted fields against user input, computes an explainable confidence score, generates evidence, records execution metadata for replay, and optionally answers questions over uploaded documents using a RAG pipeline.

Primary capabilities include:

- OCR Extraction
- Identity Verification
- Validation
- Confidence Scoring
- Evidence Generation
- Provenance Tracking
- Observability
- Deterministic Replay
- Retrieval-Augmented Generation (RAG)
- SDK Support

---

# High-Level Architecture

```text
                User Input
                     │
                     ▼
              Input Layer
                     │
                     ▼
              OCR Extraction
                     │
                     ▼
           Field Extraction
                     │
                     ▼
           Validation Layer
                     │
                     ▼
          Confidence Engine
                     │
                     ▼
           Evidence Layer
                     │
                     ▼
       Observability Layer
                     │
                     ▼
         Provenance Layer
                     │
                     ▼
          Evidence Ledger
                     │
                     ▼
          Replay Engine
                     │
                     ▼
                  SDK/API
                     │
                     ▼
                Consumers
```

---

# Repository Organization

```text
app.py

layers/
services/
sdk/
capabilities/
contracts/

templates/
static/

evaluation/
benchmarking/

learning_kit/
integration/
demo/

tests/

uploads/
vectorstore/
ledger/
metrics/
logs/

docs/
review_packets/
```

---

# Execution Flow

A verification request follows this sequence:

1. User submits document and form data.
2. Input validation checks request completeness.
3. OCR extracts raw document text.
4. Extraction layer converts raw text into structured fields.
5. Validation layer compares extracted values with user-provided values.
6. Confidence engine computes an explainable confidence score.
7. Evidence layer packages supporting validation artifacts.
8. Observability layer records metrics and trace information.
9. Provenance metadata is attached.
10. Execution snapshot is stored in the evidence ledger.
11. API returns the final response.

---

# Layer Responsibilities

## Input Layer

Responsibilities:

- Validate incoming requests
- Route requests
- Reject malformed inputs

Does NOT:

- Perform OCR
- Validate identity
- Compute confidence

---

## OCR Service

Responsibilities:

- Image preprocessing
- OCR execution
- OCR fallback logic

Does NOT:

- Validate extracted values
- Compute confidence

---

## Extraction Layer

Responsibilities:

- Parse OCR output
- Extract structured document fields
- Normalize extracted values

Does NOT:

- Validate identity
- Score confidence

---

## Validation Layer

Responsibilities:

- Compare extracted fields with user input
- Produce field-level validation results

Does NOT:

- Perform OCR
- Generate evidence

---

## Confidence Layer

Responsibilities:

- Compute explainable confidence score
- Weight validation outcomes
- Generate confidence reasoning

Does NOT:

- Perform extraction
- Modify validation results

---

## Evidence Layer

Responsibilities:

- Assemble validation artifacts
- Package supporting evidence

Does NOT:

- Alter validation decisions

---

## Observability Layer

Responsibilities:

- Logging
- Metrics
- Health monitoring
- Trace IDs

Does NOT:

- Participate in validation logic

---

## Provenance Layer

Responsibilities:

- Attach execution metadata
- Record lineage information

Does NOT:

- Modify business logic

---

## Replay Service

Responsibilities:

- Retrieve historical execution snapshots
- Reconstruct previous executions

Does NOT:

- Re-run OCR
- Re-run validation

---

# Request Lifecycle

```text
Client Request

↓

FastAPI Route

↓

Input Validation

↓

OCR

↓

Extraction

↓

Validation

↓

Confidence

↓

Evidence

↓

Observability

↓

Ledger Storage

↓

Response
```

---

# Running the Project

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Environment Variables

Required:

```env
OPENROUTER_API_KEY=YOUR_API_KEY
```

Optional variables should be documented in `.env.example` if present.

---

# Debugging Guide

## OCR Issues

Check:

- Uploaded image quality
- OCR preprocessing
- OCR provider logs

Relevant files:

```
services/ocr_service.py
```

---

## Validation Issues

Check:

```
layers/validation_layer.py
```

Confirm:

- Field normalization
- Matching logic
- Required fields

---

## Confidence Issues

Review:

```
layers/confidence_layer.py
```

Verify:

- Weight configuration
- Missing fields
- Reasoning output

---

## Replay Issues

Check:

```
ledger/
```

Confirm:

- Trace ID exists
- Snapshot integrity

---

## RAG Issues

Verify:

- Uploaded PDF
- Vector store creation
- Embedding generation
- OpenRouter connectivity

---

# Extending the Platform

## Add a New Document Type

1. Create a new handler under `capabilities/`.
2. Register it in `document_registry.py`.
3. Implement extraction rules.
4. Add validation logic.
5. Add tests.
6. Update documentation.

---

## Add a New OCR Provider

1. Implement provider wrapper in `services/`.
2. Add fallback logic.
3. Update configuration.
4. Add provider tests.

---

## Add a New AI Provider

1. Create provider wrapper.
2. Implement request interface.
3. Update configuration.
4. Verify prompt compatibility.

---

## Add a New Validator

1. Extend `validation_layer.py`.
2. Add field comparison logic.
3. Update confidence weighting.
4. Write tests.

---

## Add a New Prompt

Update:

```
services/llm_service.py
```

Ensure:

- Structured responses
- Backward compatibility

---

## Add a New Metric

Update:

```
layers/observability_layer.py
```

Register:

- Metric name
- Collection logic
- Export behavior

---

## Add a New SDK Feature

1. Extend SDK interface.
2. Keep backward compatibility.
3. Update README.
4. Update tutorials.
5. Add SDK tests.

---

# Testing

Run all tests:

```bash
pytest
```

Run specific tests:

```bash
pytest tests/test_sdk.py
```

Always ensure new functionality includes unit tests.

---

# Best Practices

- Keep business logic inside layers.
- Avoid adding business logic to API routes.
- Preserve deterministic replay.
- Update documentation with every architectural change.
- Maintain backward compatibility for SDK consumers.

---

# Common Mistakes

- Adding validation logic to OCR services.
- Modifying replay snapshots.
- Hardcoding configuration values.
- Skipping tests after changes.
- Mixing business logic into API endpoints.

---

# Additional Documentation

Refer to:

- README.md
- ARCHITECTURE_GUIDE.md
- OPERATIONS_GUIDE.md
- EXTENSION_GUIDE.md
- PRODUCTION_READINESS.md
- REVIEW_PACKET.md
- KNOWLEDGE_TRANSFER.md

These documents together form the complete engineering handover package.