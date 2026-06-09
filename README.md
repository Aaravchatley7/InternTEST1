# BHIV Multi-Input Intelligence Platform

## Overview

The BHIV Multi-Input Intelligence Platform is a reusable intelligence and validation system designed to process multiple forms of input, extract structured information, validate identities, calculate confidence scores, provide evidence-backed decisions, and answer questions from uploaded documents.

The platform combines:

- Identity Verification
- OCR-based Information Extraction
- LLM-based Field Understanding
- Validation Engine
- Confidence Scoring
- Evidence Generation
- Observability and Monitoring
- Retrieval-Augmented Generation (RAG)
- FastAPI Web Interface

This project serves as the foundation for future BHIV systems involving documents, forms, certificates, reports, invoices, structured records, and unstructured data.

---

# Architecture

## High-Level Flow

```text
User Input
    │
    ▼
Input Layer
    │
    ▼
Extraction Layer
(EasyOCR + OpenRouter LLM)
    │
    ▼
Validation Layer
    │
    ▼
Confidence Layer
    │
    ▼
Evidence Layer
    │
    ▼
Observability Layer
    │
    ▼
Trusted Output
```

---

## Identity Verification Flow

```text
User Form
+
PAN/Aadhaar Upload

        │
        ▼

OCR Extraction

        │
        ▼

LLM Information Extraction

        │
        ▼

Field Comparison

        │
        ▼

Validation Engine

        │
        ▼

Confidence Calculation

        │
        ▼

Evidence Generation

        │
        ▼

Verification Result
```

---

## RAG Flow

```text
PDF Upload

    │

    ▼

Document Loader

    │

    ▼

Chunking

    │

    ▼

Embeddings

    │

    ▼

FAISS Vector Store

    │

    ▼

Question

    │

    ▼

Similarity Search

    │

    ▼

Context Retrieval

    │

    ▼

OpenRouter LLM

    │

    ▼

Answer + Confidence
```

---

# Features

## Identity Verification

- Aadhaar Verification
- PAN Verification
- OCR-based Extraction
- LLM-based Entity Understanding
- Validation Scoring
- Confidence Scoring
- Evidence Generation
- Trace IDs

---

## Knowledge Assistant (RAG)

- PDF Upload
- Automatic Vectorization
- FAISS Storage
- Question Answering
- Retrieval-Based Context Generation
- Confidence Output

---

## Observability

- Health Endpoint
- Metrics Endpoint
- Request Tracking
- Error Tracking
- Latency Monitoring
- Trace IDs

---

## User Interface

- Dashboard
- Identity Verification Portal
- Knowledge Assistant
- Metrics Dashboard
- Health Dashboard

---

# Project Structure

```text
BHIV_Project/

│
├── app.py
│
├── layers/
│   ├── input_layer.py
│   ├── extraction_layer.py
│   ├── validation_layer.py
│   ├── confidence_layer.py
│   ├── evidence_layer.py
│   ├── rag_layer.py
│   └── observability_layer.py
│
├── services/
│   ├── ocr_service.py
│   ├── llm_service.py
│   ├── comparison_service.py
│   ├── rag_service.py
│   ├── vector_service.py
│   └── vector_builder.py
│
├── contracts/
│   ├── identity_contract_v1.json
│   ├── validation_contract_v1.json
│   └── confidence_contract_v1.json
│
├── logs/
│
├── metrics/
│
├── review_packets/
│
├── templates/
│
├── static/
│
├── uploads/
│
├── vectorstore/
│
├── tests/
│
└── README.md
```

---

# Technologies Used

## Backend

- FastAPI
- Python

## OCR

- EasyOCR

## LLM

- OpenRouter API
- GPT OSS Model

## Vector Database

- FAISS

## RAG

- LangChain

## Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

## Testing

- Pytest

---

# Environment Setup

## 1. Clone Repository

```bash
git clone <repository-url>
cd BHIV_Project
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create:

```text
.env
```

Add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# How To Run

## Start Application

```bash
uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# How To Use

## Identity Verification

1. Open:

```text
http://127.0.0.1:8000/verify-ui
```

2. Enter:

- Name
- DOB
- Email
- Phone
- Aadhaar Number
- PAN Number

3. Upload:

- Aadhaar Image
- PAN Image

4. Click:

```text
Verify Identity
```

5. View:

- Validation Result
- Validation Score
- Confidence Score
- Evidence
- Trace ID

---

## Knowledge Assistant

1. Open:

```text
http://127.0.0.1:8000/rag-ui
```

2. Upload PDF

3. Ask Questions

Examples:

```text
What is Probability?

Explain Bayes Theorem.

Summarize Chapter 3.
```

4. View:

- Answer
- Confidence

---

# API Endpoints

## Identity Verification

```http
POST /documents/verify
```

---

## Upload PDF

```http
POST /rag/upload
```

---

## Ask Question

```http
POST /rag/ask
```

---

## Health Check

```http
GET /health
```

---

## Metrics

```http
GET /metrics
```

---

# Testing

Run all tests:

```bash
pytest
```

Expected:

```text
4 passed
```

---

# Deliverables Implemented

## Phase 1

- PAN Extraction
- Aadhaar Extraction
- Validation Engine
- Comparison Engine
- Confidence Engine

## Phase 2

- Input Layer
- Extraction Layer
- Validation Layer
- Confidence Layer
- Evidence Layer
- Output Layer

## Phase 3

- RAG Pipeline
- Evidence-Based Responses

## Phase 4

- Health Endpoint
- Metrics Endpoint
- Trace IDs
- Request Monitoring

## Phase 5

- Accuracy Reporting Framework

## Phase 6

- FastAPI Deployment
- UI Integration

## Phase 7

- Review Packet
- README
- Contracts
- Documentation

---

# Future Improvements

- Passport Verification
- Multi-Document Validation
- Cloud Deployment
- OpenTelemetry Integration
- Advanced Confidence Calibration
- Continuous Evaluation Pipelines

---

# Author

Aarav Chatley

BHIV Build Cycle Submission