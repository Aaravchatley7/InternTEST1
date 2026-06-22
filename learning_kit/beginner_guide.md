# Beginner Guide

## What Is BHIV?

The BHIV Multi-Input Intelligence Platform is a reusable intelligence capability designed for:

- Identity Verification
- Document Intelligence
- Validation
- Confidence Scoring
- Evidence Generation
- Replay
- Provenance
- Retrieval-Augmented Generation (RAG)

---

# Prerequisites

Required:

- Python 3.11+
- Git
- OpenRouter API Key

Recommended:

- VS Code
- Postman

---

# Installation

Clone Repository

```bash
git clone <repository-url>
```

Navigate to Project

```bash
cd BHIV_Project
```

---

# Create Virtual Environment

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

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Create:

```text
.env
```

Add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# Running The Application

Start FastAPI Server

```bash
uvicorn app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Running Tests

Execute:

```bash
pytest
```

Expected:

```text
All tests passing
```

---

# Project Structure

```text
layers/
services/
sdk/
capabilities/
evaluation/
benchmarking/
tests/
templates/
static/
ledger/
```

---

# Typical Workflow

1. Upload Document
2. OCR Extraction
3. Field Extraction
4. Validation
5. Confidence Calculation
6. Evidence Generation
7. Ledger Storage
8. Replay Capability

---

# Debugging Tips

Check:

```text
logs/app.log
```

Check:

```text
metrics/metrics.json
```

Check:

```text
ledger/
```

Check:

```text
review_packets/
```

---

# Useful Endpoints

Health

```http
GET /health
```

Metrics

```http
GET /metrics
```

Verification

```http
POST /documents/verify
```

Replay

```http
GET /replay/{trace_id}
```

RAG Upload

```http
POST /rag/upload
```

RAG Ask

```http
POST /rag/ask
```

---

# First Learning Goal

A new developer should be able to:

- Run the platform
- Verify an Aadhaar document
- Verify a PAN document
- Generate a trace ID
- Replay a historical decision
- Run all tests

without external assistance.