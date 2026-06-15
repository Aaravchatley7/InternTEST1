# Deployment Architecture

## Architecture Overview

```text
Browser/UI

      │

      ▼

FastAPI Application

      │

      ├── Verification Capability
      │
      ├── Validation Capability
      │
      ├── Confidence Capability
      │
      ├── Evidence Capability
      │
      ├── Observability Capability
      │
      └── RAG Capability

      │

      ▼

External Dependencies

      ├── OpenRouter
      ├── EasyOCR
      ├── Tesseract
      ├── FAISS
      └── LangChain
```

---

# Runtime Components

Application Layer

* FastAPI

Intelligence Layer

* OCR
* Validation
* Confidence
* Evidence

Knowledge Layer

* RAG

Observability Layer

* Logging
* Metrics
* Traceability

---

# Deployment Model

Current:

Local Deployment

Future:

API Service

Shared Capability Service

Sidecar Deployment

---

# Conclusion

The architecture supports standalone deployment and future ecosystem integration.
