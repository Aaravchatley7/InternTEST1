# BHIV Multi-Input Intelligence Platform

## Overview

The BHIV Multi-Input Intelligence Platform is a reusable intelligence, validation, and document understanding system developed as part of the BHIV engineering build cycle.

The platform combines identity verification, confidence scoring, evidence generation, observability, retrieval-augmented generation (RAG), and reusable validation capabilities into a single deployable architecture.

The system is designed to serve as a foundation for future BHIV products involving:

* Identity Documents
* Certificates
* Forms
* Structured Records
* Reports
* Invoices
* Knowledge Repositories

---

# Architecture

## High-Level Architecture

```text
User Input
    │
    ▼
Input Layer
    │
    ▼
Extraction Layer
(OCR + Regex Recovery + LLM)
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

## Identity Verification Pipeline

```text
User Form
+
Document Upload

        │
        ▼

OCR Extraction
(EasyOCR + Tesseract)

        │
        ▼

Regex Recovery Layer
(Aadhaar / PAN / DOB)

        │
        ▼

LLM Extraction Layer
(OpenRouter)

        │
        ▼

Field Fusion Engine

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

Verification Output
```

---

## RAG Pipeline

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

## Multi-Input Foundation

The platform now includes a reusable capability registry to support future expansion.

Supported Input Types:

* Documents
* Images
* Forms
* Structured JSON

Future BHIV systems can reuse the same validation and confidence framework without architectural changes.

---

# Major Features

## Identity Verification

* Aadhaar Verification
* PAN Verification
* OCR Extraction
* Regex-Based Recovery
* LLM-Based Extraction
* Validation Scoring
* Confidence Scoring
* Evidence Generation
* Trace IDs

---

## Validation Hardening

Implemented:

* Fuzzy Name Matching
* Aadhaar Normalization
* PAN Normalization
* DOB Normalization
* Phone Normalization
* Typo Tolerance
* Confidence Weighting

---

## Accuracy Recovery

Implemented:

* OCR Preprocessing
* EasyOCR Support
* Tesseract Fallback
* Aadhaar Regex Recovery
* PAN Regex Recovery
* DOB Recovery
* Field Fusion Logic

---

## Knowledge Assistant (RAG)

* PDF Upload
* Automatic Vectorization
* FAISS Storage
* Similarity Search
* Context Retrieval
* Question Answering
* Confidence Output

---

## Observability

* Health Endpoint
* Metrics Endpoint
* Request Tracking
* Error Tracking
* Latency Monitoring
* Logging
* Trace IDs

---

# Project Structure

```text
BHIV_Project/

├── app.py

├── capabilities/
│   ├── input_registry.py
│   ├── input_contract_v1.json
│   └── validation_contract_v2.json

├── contracts/
│   ├── identity_contract_v1.json
│   ├── validation_contract_v1.json
│   ├── confidence_contract_v1.json
│   └── evidence_contract_v1.json

├── layers/
│   ├── input_layer.py
│   ├── extraction_layer.py
│   ├── validation_layer.py
│   ├── confidence_layer.py
│   ├── evidence_layer.py
│   ├── rag_layer.py
│   └── observability_layer.py

├── services/
│   ├── ocr_service.py
│   ├── llm_service.py
│   ├── comparison_service.py
│   ├── rag_service.py
│   ├── vector_service.py
│   └── vector_builder.py

├── reports/
│   ├── accuracy_report.md
│   ├── validation_accuracy_report.md
│   └── deployment_report.md

├── tests/

├── review_packets/

├── uploads/

├── vectorstore/

└── README.md
```

---

# Technologies Used

Backend:

* FastAPI
* Python

OCR:

* EasyOCR
* Tesseract OCR

LLM:

* OpenRouter
* GPT OSS

Vector Database:

* FAISS

RAG Framework:

* LangChain

Frontend:

* HTML
* CSS
* JavaScript
* Jinja2

Testing:

* Pytest

---

# Testing

Current Test Coverage Includes:

* OCR Extraction
* Aadhaar Recovery
* PAN Recovery
* Validation Logic
* Confidence Scoring
* Identity Pipeline
* Health Checks
* Metrics Validation
* Observability
* Trace ID Generation
* RAG Functionality

Target Achieved:

10+ Automated Tests

Run:

```bash
pytest
```

---

# Reports

Generated Reports:

* accuracy_report.md
* validation_accuracy_report.md
* deployment_report.md
* REVIEW_PACKET.md

---

# Deliverables Implemented

## Phase 1 – Accuracy Recovery

* OCR Improvements
* Aadhaar Recovery
* PAN Recovery
* Extraction Fallback Logic
* Accuracy Reporting

## Phase 2 – Validation Hardening

* Fuzzy Matching
* Normalization
* Confidence Weighting

## Phase 3 – Multi-Input Foundation

* Capability Registry
* Input Contracts
* Validation Contract V2

## Phase 4 – Testing

* Expanded Test Coverage
* Identity Pipeline Testing
* Health Testing
* Metrics Testing

## Phase 5 – Deployment

* FastAPI Deployment
* Deployment Evidence
* Endpoint Validation

## Phase 6 – Documentation

* README
* REVIEW_PACKET
* Accuracy Report
* Validation Report
* Deployment Report

---

# Future Enhancements

* Passport Verification
* Invoice Verification
* Certificate Verification
* OpenTelemetry Integration
* Cloud Deployment
* Continuous Evaluation Pipelines

---

# Author

Aarav Chatley

BHIV Multi-Input Intelligence Platform
Task 1 → Task 4 Repository Continuation
