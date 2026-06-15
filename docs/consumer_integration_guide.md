# Consumer Integration Guide

## Purpose

Provide future teams with integration guidance for consuming the BHIV Multi-Input Intelligence Platform.

---

# Available Capabilities

## Identity Verification

Inputs:

* Aadhaar
* PAN

Outputs:

* Validation Result
* Validation Score
* Confidence Score
* Evidence Package
* Provenance Metadata

---

## Knowledge Assistant

Inputs:

* PDF Documents
* User Questions

Outputs:

* Answer
* Confidence Score
* Provenance Metadata

---

# Required Metadata

Consumers should preserve:

* trace_id
* request_id
* schema_version
* contract_version
* evaluation_version

---

# Integration Models

## Embedded

Use when:

* Tight coupling is required
* Low latency is required

---

## API Linked

Use when:

* Capability reuse is desired
* Independent deployment is preferred

---

## Sidecar

Use when:

* Independent scaling is required
* Traceability must be preserved

---

# Assumptions

Consumers are responsible for:

* Business decisions
* Governance decisions
* Policy decisions
* User authorization

The capability is responsible for:

* Extraction
* Validation
* Confidence
* Evidence

---

# Recommended Usage Pattern

```text
Consumer

   │

   ▼

BHIV Capability

   │

   ▼

Validation

   │

   ▼

Confidence

   │

   ▼

Evidence

   │

   ▼

Consumer Decision
```

---

# Conclusion

Consumers should treat outputs as intelligence artifacts rather than governance authority.
