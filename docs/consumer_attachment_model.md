# Consumer Attachment Model

## Purpose

Define how future BHIV systems can consume and integrate the capability.

---

# Attachment Modes

## Embedded

Description:

Capability is integrated directly into the consuming application.

Examples:

* UniGuru
* Parikshak

Advantages:

* Low latency
* Tight integration

---

## API Linked

Description:

Capability is deployed independently and consumed through APIs.

Examples:

* Verification Systems
* Knowledge Platforms

Advantages:

* Reusable
* Independent deployment

---

## Sidecar

Description:

Capability operates alongside another service.

Examples:

* Signals Corps
* Monitoring Systems

Advantages:

* Isolation
* Independent scaling

---

## Reusable Capability Service

Description:

Capability acts as a shared platform component.

Examples:

* Future BHIV Products

Advantages:

* Centralized maintenance
* Consistent validation behavior

---

# Consumer Requirements

## UniGuru

Inputs:

* Student Documents
* Forms

Outputs:

* Validation
* Confidence
* Evidence

---

## Parikshak

Inputs:

* Examination Records
* Verification Documents

Outputs:

* Validation
* Evidence

---

## Signals Corps

Inputs:

* Reports
* Documents

Outputs:

* Extraction
* Confidence
* Traceability

---

## Verification Systems

Inputs:

* Identity Documents

Outputs:

* Validation
* Confidence
* Evidence

---

## Knowledge Platforms

Inputs:

* PDF Documents

Outputs:

* Answers
* Confidence Scores

---

# Integration Assumptions

All consumers must:

* Provide supported inputs
* Respect authority boundaries
* Treat confidence as probabilistic
* Preserve provenance metadata

---

# Conclusion

The capability is designed for reuse across multiple BHIV products through embedded, API-linked, sidecar, or shared-service integration models.
