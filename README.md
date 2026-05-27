# DocVerify — AI-Powered Document Verification System

## Overview
Verifies identity by OCR-reading Aadhaar, PAN, or Passport documents and comparing extracted fields (name, DOB, ID numbers) against form input.

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in:
- `OPENROUTER_API_KEY` — from openrouter.ai
- `SMTP_EMAIL` / `SMTP_PASSWORD` — Gmail + App Password
- `SECRET_KEY` — any random string

## Run

```bash
python app.py
```

Open http://localhost:5000

## Architecture

| File | Role |
|------|------|
| `app.py` | Flask routes, file uploads, session |
| `ocr_utils.py` | EasyOCR text extraction |
| `llm_utils.py` | OpenRouter LLM field extraction (JSON) |
| `compare_utils.py` | Field normalization & matching |
| `langgraph_flow.py` | Orchestration pipeline |
| `email_utils.py` | Rich HTML email sending |
| `config.py` | Env-based configuration |

## Fields Verified
- ✅ Full Name
- ✅ Date of Birth
- ✅ Aadhaar Number
- ✅ PAN Number
- ✅ Phone (if present in document)
