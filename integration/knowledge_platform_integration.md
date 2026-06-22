# Knowledge Platform Integration

## Purpose

Provide document understanding and question answering.

---

# Use Cases

- Academic Content
- Research Papers
- Policy Documents
- Training Material

---

# Integration Model

```text
Knowledge Platform
    ↓
BHIV RAG API
    ↓
Answer + Confidence
```

---

# APIs

POST /rag/upload

POST /rag/ask

GET /health