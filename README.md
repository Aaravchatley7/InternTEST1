# BHIV Multi-Input Intelligence Platform

## Overview

The BHIV Multi-Input Intelligence Platform is a reusable intelligence capability designed for document verification, validation, confidence scoring, evidence generation, provenance tracking, observability, deterministic replay, and Retrieval-Augmented Generation (RAG).

The platform has evolved from a document verification system into a reusable BHIV ecosystem capability that can be integrated into future products and extended by new engineers with minimal onboarding.

---

# Core Capabilities

## Identity Verification

Supported Documents:

- Aadhaar
- PAN

Framework Support:

- Passport
- Driving Licence
- Voter ID
- Educational Certificates
- Invoices
- Government Forms

Features:

- OCR Extraction
- Identity Validation
- Confidence Scoring
- Evidence Generation
- Replay Support

---

## Confidence Engine

Generates:

- Confidence Score
- Confidence Level
- Confidence Reasoning
- Weight Attribution

Example:

```json
{
    "score": 0.95,
    "level": "HIGH",
    "reasoning": [
        "Name matched",
        "DOB matched",
        "PAN matched"
    ]
}
```

---

## Evidence Generation

Produces evidence-backed validation outputs.

Includes:

- Validation Artifacts
- Confidence Artifacts
- Trace Metadata
- Replay Artifacts

---

## Observability

Provides:

- Logging
- Metrics
- Health Monitoring
- Trace IDs
- Latency Tracking

---

## Provenance

Tracks:

- trace_id
- request_id
- schema_version
- contract_version
- evaluation_version
- timestamp
- origin_source
- confidence_source

---

## Deterministic Replay

Allows reconstruction of historical executions using trace IDs.

Replay reconstructs:

- Original Request
- Extraction Output
- Validation Output
- Confidence Output
- Evidence Output
- Final Response

without re-running OCR, extraction, validation, or confidence workflows.

---

## Retrieval-Augmented Generation (RAG)

Supports:

- PDF Upload
- Document Chunking
- Embeddings
- Vector Search
- Question Answering

---

# Architecture

## High-Level Architecture

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

## Verification Flow

```text
User Form
+
Document

    ↓

OCR Extraction

    ↓

Field Extraction

    ↓

Validation

    ↓

Confidence

    ↓

Evidence

    ↓

Ledger Storage

    ↓

Response
```

---

## Replay Flow

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

## RAG Flow

```text
PDF Upload

    ↓

Chunking

    ↓

Embeddings

    ↓

FAISS

    ↓

Retrieval

    ↓

OpenRouter LLM

    ↓

Answer
```

---

# Capability SDK

The platform exposes reusable SDK interfaces.

## Verification SDK

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

## RAG SDK

```python
from sdk.rag_sdk import RAGSDK

rag = RAGSDK()

answer = rag.ask(
    question
)
```

---

# Capability Registry

Document capabilities are managed through:

```text
capabilities/document_registry.py
```

Supported:

- Aadhaar
- PAN
- Passport
- Driving Licence
- Voter ID
- Certificate
- Invoice
- Government Form

---

# Project Structure

```text
BHIV_Project/

├── app.py

├── sdk/

├── capabilities/

├── layers/

├── services/

├── contracts/

├── evaluation/

├── benchmarking/

├── learning_kit/

├── demo/

├── integration/

├── tests/

├── ledger/

├── metrics/

├── logs/

├── uploads/

├── vectorstore/

├── templates/

├── static/

└── review_packets/
```

---

# Technologies Used

## Backend

- FastAPI
- Python

## OCR

- EasyOCR
- Tesseract

## LLM

- OpenRouter
- GPT OSS

## Vector Database

- FAISS

## RAG

- LangChain

## Frontend

- HTML
- CSS
- JavaScript
- Jinja2

## Testing

- Pytest

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create:

```text
.env
```

Add:

```env
OPENROUTER_API_KEY=your_api_key
```

---

# Running The Platform

```bash
uvicorn app:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Verification

```http
POST /documents/verify
```

---

## Replay

```http
GET /replay/{trace_id}
```

---

## Health

```http
GET /health
```

---

## Metrics

```http
GET /metrics
```

---

## RAG Upload

```http
POST /rag/upload
```

---

## RAG Question

```http
POST /rag/ask
```

---

## Supported Documents

```http
GET /capabilities/documents
```

---

# Deterministic Replay

Replay allows reconstruction of historical executions.

Example:

```http
GET /replay/{trace_id}
```

Returns:

```json
{
    "request": {},
    "extraction": {},
    "validation": {},
    "confidence": {},
    "evidence": {},
    "output": {}
}
```

---

# Benchmarking

Location:

```text
benchmarking/
```

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- False Positive Rate
- False Negative Rate

Generated Through:

```text
evaluation/run_evaluation.py
```

---

# Learning Kit

Location:

```text
learning_kit/
```

Includes:

- Architecture Guide
- Beginner Guide
- Learning Roadmap
- Troubleshooting Guide
- Module Tutorials
- Hands-On Exercises

Purpose:

Enable self-paced onboarding.

---

# Demonstration Suite

Location:

```text
demo/
```

Includes:

- Sample Requests
- Sample Outputs
- Walkthroughs
- Verification Examples
- Replay Examples
- RAG Examples

---

# Ecosystem Integration

Integration Guides Provided For:

- UniGuru
- Parikshak
- Government Verification Systems
- Knowledge Platforms
- Document Intelligence Systems

Location:

```text
integration/
```

---

# Testing

Run:

```bash
pytest
```

Coverage Includes:

- Validation
- OCR Recovery
- Confidence
- Replay
- Replay Determinism
- Evidence Ledger
- Metrics
- Health
- RAG
- SDK

---

# Deployment Evidence

Deployment validation includes:

- Application Startup
- Health Endpoint
- Metrics Endpoint
- Verification Endpoint
- Replay Endpoint
- RAG Endpoint

Evidence available in:

```text
review_packets/screenshots/
```

---

# Design Principles

The platform is built around:

- Reusability
- Explainability
- Traceability
- Replayability
- Observability
- Extensibility
- Ecosystem Integration

---

# Future Enhancements

Potential future work:

- Additional Document Types
- OCR Provider Expansion
- Confidence Calibration
- Cloud Deployment
- Distributed Tracing
- Advanced Benchmarking
- ML-Based Document Classification

---

# Author

Aarav Chatley

Applied AI Engineering

BHIV Multi-Input Intelligence Platform

Version 1.0.0
