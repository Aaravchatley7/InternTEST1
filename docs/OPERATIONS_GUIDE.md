# Operations Guide

## BHIV Multi-Input Document Intelligence Platform

Version: 1.0.0

Status: Production Handover

---

# Purpose

This document provides operational guidance for deploying, configuring, monitoring, maintaining, and troubleshooting the BHIV Multi-Input Document Intelligence Platform.

It is intended for engineers responsible for operating the platform in development, staging, or production environments.

---

# System Requirements

## Operating System

Supported:

- Windows 10/11
- Ubuntu 22.04+
- macOS 13+

---

## Python

Recommended:

```
Python 3.11+
```

---

## Required Dependencies

Install using:

```bash
pip install -r requirements.txt
```

Major dependencies include:

- FastAPI
- Uvicorn
- EasyOCR
- pytesseract
- OpenCV
- LangChain
- FAISS
- OpenRouter SDK
- Pytest

---

# Environment Configuration

Create a `.env` file in the project root.

Required variables:

```env
OPENROUTER_API_KEY=YOUR_API_KEY
```

Optional variables may include logging level or model configuration depending on deployment.

Never commit `.env` files to version control.

---

# Application Startup

## Development Mode

```bash
uvicorn app:app --reload
```

---

## Production Mode

Example:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

For production deployments, use a process manager such as Gunicorn (Linux) or a Windows service wrapper.

---

# Verifying Startup

After starting the application, verify the following:

| Endpoint | Expected Result |
|-----------|-----------------|
| `/` | Home page loads |
| `/docs` | Swagger UI accessible |
| `/health` | Healthy response |
| `/metrics` | Metrics available |
| `/documents/verify` | Accepts requests |
| `/replay/{trace_id}` | Replay available |
| `/rag/upload` | Upload endpoint operational |
| `/rag/ask` | Question answering operational |

---

# Health Checks

Health endpoint:

```http
GET /health
```

The endpoint should verify:

- Application startup
- OCR availability
- Upload directory
- Ledger directory
- Vector store availability
- Metrics subsystem

A healthy response indicates that critical components are operational.

---

# Metrics

Metrics endpoint:

```http
GET /metrics
```

Current metrics include:

- Total requests
- Successful requests
- Failed requests
- Average latency
- Replay requests
- RAG requests

These metrics help identify system behavior and performance trends.

---

# Logging

Logs are stored in:

```text
logs/
```

Logs should capture:

- Request ID
- Trace ID
- Endpoint
- Processing time
- Validation outcome
- Errors
- Warnings

Sensitive document contents should not be logged.

---

# Trace IDs

Every verification request should generate a unique Trace ID.

Purpose:

- Debugging
- Replay
- Evidence tracking
- Provenance

Always include the Trace ID when investigating issues.

---

# Evidence Ledger

Execution snapshots are stored in:

```text
ledger/
```

Each record contains:

- Request
- Extraction
- Validation
- Confidence
- Evidence
- Final response

These artifacts enable deterministic replay and auditing.

---

# Replay Operations

Replay endpoint:

```http
GET /replay/{trace_id}
```

Replay reconstructs the stored execution without invoking OCR, validation, or confidence computation again.

Use replay when:

- Investigating bugs
- Reviewing historical decisions
- Comparing outputs
- Demonstrating deterministic behavior

---

# Backup Strategy

Recommended backup targets:

- `ledger/`
- `vectorstore/`
- `logs/`
- Configuration files
- Documentation
- Evaluation datasets

Backups should be scheduled regularly in production environments.

---

# Dependency Management

To update dependencies:

```bash
pip install -U <package>
```

After updating:

1. Run the full test suite.
2. Verify all endpoints.
3. Validate replay behavior.
4. Update documentation if interfaces change.

Avoid upgrading multiple critical libraries simultaneously without testing.

---

# Version Upgrade Process

Before upgrading:

- Backup the repository.
- Backup the ledger.
- Backup the vector store.

Upgrade process:

1. Create a feature branch.
2. Update dependencies.
3. Execute all tests.
4. Verify API compatibility.
5. Review replay integrity.
6. Merge after validation.

---

# Monitoring Checklist

Regularly monitor:

- Application uptime
- API response latency
- Error rate
- OCR failures
- Replay success rate
- Disk usage
- Vector store size
- Ledger growth

---

# Failure Recovery

## Application Fails to Start

Check:

- Python version
- Installed dependencies
- Environment variables
- Port availability

---

## OCR Failure

Verify:

- Image quality
- EasyOCR installation
- Tesseract installation
- OCR logs

---

## Validation Failure

Check:

- Extracted fields
- Validation rules
- Input normalization

---

## Replay Failure

Verify:

- Trace ID exists
- Ledger file integrity
- JSON parsing

---

## RAG Failure

Check:

- Uploaded document
- Vector store generation
- Embeddings
- OpenRouter connectivity

---

# Performance Considerations

The current implementation is intended for moderate workloads.

Potential optimizations:

- OCR request queue
- Caching
- Database-backed metrics
- Distributed logging
- Parallel document processing

---

# Security Considerations

Recommended practices:

- Protect API keys.
- Restrict upload size.
- Validate uploaded file types.
- Sanitize filenames.
- Do not log personally identifiable information.
- Rotate credentials periodically.

Current implementation focuses on engineering demonstration rather than hardened production security.

---

# Operational Risks

Known risks include:

- OCR quality degradation on poor images.
- External LLM availability.
- Local filesystem dependence.
- Limited evaluation dataset.
- File-based metrics persistence.

These risks should be addressed before large-scale production deployment.

---

# Incident Response

When an issue is reported:

1. Record the Trace ID.
2. Review logs.
3. Execute replay.
4. Compare evidence output.
5. Identify the failing layer.
6. Apply fixes.
7. Re-run tests.
8. Update documentation if behavior changes.

---

# Routine Maintenance

Recommended schedule:

Daily:

- Review logs
- Monitor health endpoint

Weekly:

- Review metrics
- Verify replay functionality
- Inspect ledger growth

Monthly:

- Update dependencies
- Expand evaluation dataset
- Archive old logs
- Review documentation

---

# Operational Best Practices

- Preserve deterministic replay.
- Maintain backward compatibility.
- Keep documentation synchronized with implementation.
- Avoid introducing business logic into API routes.
- Validate all operational changes through automated tests.

---

# Summary

The BHIV Multi-Input Document Intelligence Platform provides operational capabilities for verification, observability, replay, and knowledge retrieval. This guide establishes the standard procedures required to deploy, monitor, maintain, and troubleshoot the system while ensuring operational continuity for future engineering teams.