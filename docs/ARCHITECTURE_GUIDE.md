# Architecture Guide

## BHIV Multi-Input Document Intelligence Platform

Version: 1.0.0

Status: Canonical Architecture

---

# Purpose

This document defines the canonical architecture of the BHIV Multi-Input Document Intelligence Platform.

It serves as the single source of truth for how the platform is organized, how data flows through the system, where responsibilities begin and end, and how future engineers should safely extend the platform.

This document supersedes any previous architecture diagrams or descriptions.

---

# High-Level Architecture

```text
                    User Request
                         │
                         ▼
                  FastAPI Endpoint
                         │
                         ▼
                   Input Layer
                         │
                         ▼
                  OCR Providers
                         │
                         ▼
                Extraction Layer
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
                     SDK Layer
                         │
                         ▼
              External Consumers
```

---

# Complete Request Lifecycle

```text
Client

↓

FastAPI Router

↓

Input Validation

↓

OCR

↓

Field Extraction

↓

Validation

↓

Confidence Calculation

↓

Evidence Generation

↓

Metrics + Logging

↓

Provenance Metadata

↓

Ledger Storage

↓

API Response

↓

Replay (Optional)

↓

SDK / Consumer
```

---

# Architectural Principles

The platform is built around the following engineering principles:

- Separation of Concerns
- Layered Architecture
- Explainability
- Deterministic Replay
- Extensibility
- Modularity
- Observability
- Reusability

Each layer has clearly defined responsibilities and ownership boundaries.

---

# Layer Specifications

---

# 1. Input Layer

## Purpose

Accept and validate incoming API requests before business processing begins.

## Inputs

- User form data
- Uploaded documents
- API requests

## Outputs

- Validated request object

## Dependencies

- FastAPI
- Pydantic
- Request schemas

## Extension Points

- Additional request validators
- Authentication middleware
- File validation

## Does NOT Own

- OCR
- Validation
- Confidence
- Business rules

---

# 2. OCR Layer

## Purpose

Extract textual information from uploaded documents.

## Inputs

- Image
- PDF
- Document file

## Outputs

- Raw extracted text

## Dependencies

- EasyOCR
- Tesseract
- OpenCV

## Extension Points

- Google Vision
- Azure OCR
- AWS Textract
- Custom OCR providers

## Does NOT Own

- Field extraction
- Validation
- Confidence scoring

---

# 3. Extraction Layer

## Purpose

Convert OCR text into structured document fields.

## Inputs

- OCR output

## Outputs

- Structured JSON

Example:

```json
{
    "name": "",
    "dob": "",
    "aadhaar": ""
}
```

## Dependencies

- OCR Service
- LLM Service
- Regex extraction

## Extension Points

- New document extractors
- New parsing strategies
- Field normalization

## Does NOT Own

- Validation
- Confidence
- Evidence

---

# 4. Validation Layer

## Purpose

Verify extracted fields against submitted user information.

## Inputs

- Structured extraction
- User input

## Outputs

- Validation result

Example:

```json
{
    "name": true,
    "dob": true,
    "aadhaar": false
}
```

## Dependencies

- Extraction Layer

## Extension Points

- New validators
- Fuzzy matching
- Rule engine

## Does NOT Own

- OCR
- Confidence
- Logging

---

# 5. Confidence Layer

## Purpose

Produce an explainable confidence score.

## Inputs

- Validation output

## Outputs

```json
{
    "score":0.94,
    "level":"HIGH",
    "reasoning":[]
}
```

## Dependencies

- Validation Layer

## Extension Points

- New weighting schemes
- Calibration
- Statistical confidence

## Does NOT Own

- Validation
- Evidence
- OCR

---

# 6. Evidence Layer

## Purpose

Package supporting evidence for every verification result.

## Inputs

- Validation
- Confidence

## Outputs

Evidence object

## Dependencies

- Confidence Layer

## Extension Points

- Additional artifacts
- Audit evidence
- Compliance metadata

## Does NOT Own

- Business decisions
- Replay
- Logging

---

# 7. Observability Layer

## Purpose

Monitor system execution.

## Inputs

- Request lifecycle events

## Outputs

- Logs
- Metrics
- Health status
- Trace IDs

## Dependencies

- Logging framework

## Extension Points

- Prometheus
- Grafana
- OpenTelemetry

## Does NOT Own

- Validation
- Confidence
- Replay

---

# 8. Provenance Layer

## Purpose

Track execution lineage.

## Inputs

- Request metadata
- Processing metadata

## Outputs

```json
{
    "trace_id":"",
    "request_id":"",
    "timestamp":""
}
```

## Dependencies

- Observability

## Extension Points

- Additional lineage metadata
- Version tracking

## Does NOT Own

- Business logic
- Validation
- Evidence

---

# 9. Evidence Ledger

## Purpose

Persist execution snapshots.

## Inputs

- Provenance
- Evidence
- Validation
- Confidence

## Outputs

Replayable artifacts

## Dependencies

- File storage

## Extension Points

- Database storage
- Cloud storage
- Object storage

## Does NOT Own

- Replay logic
- Validation
- OCR

---

# 10. Replay Engine

## Purpose

Reconstruct historical executions using stored artifacts.

## Inputs

- Trace ID

## Outputs

Historical execution

## Dependencies

- Evidence Ledger

## Extension Points

- Replay comparison
- Historical analytics
- Timeline reconstruction

## Does NOT Own

- OCR execution
- Validation
- Confidence generation

---

# 11. SDK Layer

## Purpose

Expose reusable interfaces for external consumers.

## Inputs

- Consumer requests

## Outputs

Platform APIs

## Dependencies

- Internal layers

## Extension Points

- New SDK methods
- Language bindings
- Client libraries

## Does NOT Own

- Business logic
- Validation implementation

---

# Consumer Layer

Consumers may include:

- Web applications
- Government systems
- Internal BHIV products
- Enterprise integrations
- Learning platforms

Consumers interact only through APIs or SDKs and should not directly depend on internal implementation details.

---

# Data Ownership

| Layer | Owns |
|---------|------|
| Input | Request validation |
| OCR | Raw text extraction |
| Extraction | Structured fields |
| Validation | Field comparison |
| Confidence | Confidence score |
| Evidence | Supporting artifacts |
| Observability | Logs and metrics |
| Provenance | Execution lineage |
| Ledger | Persistent execution records |
| Replay | Historical reconstruction |
| SDK | Public interfaces |

---

# Extension Philosophy

Future enhancements should preserve:

- Layer independence
- Clear ownership boundaries
- Deterministic replay
- Explainable confidence
- Backward-compatible SDKs

New functionality should be introduced by extending existing layers rather than bypassing them.

---

# Architecture Decision Summary

| Principle | Decision |
|------------|----------|
| Layered Design | Adopted |
| Modular Components | Adopted |
| Explainable AI | Adopted |
| Deterministic Replay | Adopted |
| Evidence-Based Validation | Adopted |
| SDK Abstraction | Adopted |
| Separation of Concerns | Adopted |

---

# Summary

The BHIV Multi-Input Document Intelligence Platform follows a modular layered architecture that separates concerns across input handling, OCR, extraction, validation, confidence scoring, evidence generation, observability, provenance, replay, and SDK exposure.

Each layer has clearly defined responsibilities, explicit ownership boundaries, and documented extension points, allowing future engineers to extend the platform safely without impacting unrelated components. This architecture serves as the canonical reference for all future development and maintenance.