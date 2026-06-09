# REVIEW_PACKET.md

# BHIV Multi-Input Intelligence Platform

## Project Overview

This project implements a reusable Multi-Input Intelligence and Validation Capability.

The system accepts structured and unstructured inputs, extracts information, validates identities, calculates confidence scores, provides evidence-backed responses, and generates trusted outputs.

---

## Entry Point

app.py

---

## Core Workflow

User Input

↓

Input Layer

↓

OCR Extraction Layer

↓

LLM Extraction Layer

↓

Validation Layer

↓

Confidence Layer

↓

Evidence Layer

↓

Observability Layer

↓

Trusted Output

---

## Major Components

### Input Layer

Validates uploaded files and incoming requests.

### Extraction Layer

Uses OCR and OpenRouter LLMs to extract structured identity information.

### Validation Layer

Compares extracted document information against user-provided information.

### Confidence Layer

Generates confidence scores based on extraction quality and validation outcomes.

### Evidence Layer

Produces evidence explaining why a validation decision was made.

### Observability Layer

Tracks metrics, latency, errors, and traceability.

### RAG Layer

Provides evidence-backed document question answering using FAISS vector search and OpenRouter.

---

## API Endpoints

### POST /documents/verify

Performs identity verification.

### POST /rag/upload

Uploads a PDF into the vector database.

### POST /rag/ask

Answers questions from uploaded documents.

### GET /health

Returns system health information.

### GET /metrics

Returns system metrics.

---

## Testing

Run:

pytest

---

## Deployment

uvicorn app:app --reload

---

## Known Limitations

OCR performance depends on image quality.

Confidence scores are heuristic-based.

RAG performance depends on uploaded document quality.

---

## Future Enhancements

OpenTelemetry integration

Cloud deployment

Redis-backed metrics

Multi-document validation

Continuous evaluation pipelines
