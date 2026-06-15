# Ecosystem Attachment Map

## Purpose

Define how the BHIV Multi-Input Intelligence Platform attaches to and interacts with future BHIV ecosystem products.

---

# Capability Classification

Type:

Reusable Intelligence Capability

Deployment Model:

* Embedded
* API Linked
* Sidecar
* Shared Service

---

# Ecosystem Placement

```text
BHIV Ecosystem

│
├── UniGuru
│
├── Parikshak
│
├── Signals Corps
│
├── Verification Systems
│
├── Knowledge Platforms
│
└── BHIV Multi-Input Intelligence Platform
       │
       ├── Extraction
       ├── Validation
       ├── Confidence
       ├── Evidence
       ├── Provenance
       └── Observability
```

---

# Consumer Relationships

## UniGuru

Consumes:

* Validation
* Confidence
* Evidence

Attachment Type:

Embedded / API

---

## Parikshak

Consumes:

* Validation
* Evidence

Attachment Type:

API

---

## Signals Corps

Consumes:

* Extraction
* Traceability
* Confidence

Attachment Type:

Sidecar

---

## Verification Systems

Consumes:

* Verification
* Confidence
* Evidence

Attachment Type:

Shared Service

---

## Knowledge Platforms

Consumes:

* RAG
* Retrieval
* Confidence

Attachment Type:

API

---

# Integration Principles

All consumers must:

* Preserve provenance metadata
* Respect authority boundaries
* Preserve traceability
* Use contract versions

---

# Conclusion

The capability is designed as a reusable ecosystem component rather than a standalone product.
