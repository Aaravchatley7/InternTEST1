# Extension Guide

## BHIV Multi-Input Document Intelligence Platform

Version: 1.0.0

Status: Engineering Handover

---

# Purpose

This document explains how future engineers can safely extend the BHIV Multi-Input Document Intelligence Platform while preserving its modular architecture, deterministic replay, and backward compatibility.

Extensions should follow the existing layered architecture. New functionality should be added by extending the appropriate layer rather than modifying unrelated components.

---

# Extension Principles

Every new capability should:

- Follow the layered architecture.
- Preserve deterministic replay.
- Remain backward compatible.
- Include automated tests.
- Update documentation.
- Register itself through the capability registry where applicable.

Avoid introducing business logic directly into API routes.

---

# General Extension Workflow

Most new capabilities follow this process:

```text
Requirement

↓

Capability Design

↓

Implementation

↓

Registration

↓

Testing

↓

Documentation

↓

Review
```

---

# Adding a New Document Type

Examples:

- Passport
- Driving Licence
- Voter ID
- Certificates
- Invoices
- Government Forms

## Files to Modify

```
capabilities/
document_registry.py
layers/extraction_layer.py
layers/validation_layer.py
services/ocr_service.py (if needed)
tests/
```

---

## Steps

1. Create a new handler under `capabilities/`.
2. Define extraction logic.
3. Implement validation rules.
4. Register the handler in `document_registry.py`.
5. Add representative test cases.
6. Update documentation.

---

## Expected Interface

Example:

```python
class PassportHandler:

    def extract(self, text):
        ...

    def validate(self, extracted, user_data):
        ...
```

---

## Testing Checklist

- OCR extraction
- Field extraction
- Validation
- Confidence score
- Replay
- SDK compatibility

---

## Acceptance Criteria

- Document successfully extracts fields.
- Validation produces expected output.
- Replay reproduces identical results.
- Tests pass.
- Documentation updated.

---

# Adding a New OCR Provider

Examples:

- Google Vision
- Azure OCR
- AWS Textract

## Files to Modify

```
services/
config.py
requirements.txt
tests/
```

---

## Steps

1. Create provider wrapper.
2. Standardize output format.
3. Add provider selection logic.
4. Configure fallback behavior.
5. Add provider-specific tests.

---

## Interface

```python
class OCRProvider:

    def extract_text(document):
        pass
```

---

## Testing Checklist

- OCR accuracy
- Error handling
- Timeout handling
- Fallback behavior

---

## Acceptance Criteria

- Provider integrates without changing downstream layers.
- Replay behavior remains unchanged.

---

# Adding a New AI Provider

Examples:

- OpenAI
- Anthropic
- Gemini
- Azure OpenAI

## Files to Modify

```
services/llm_service.py
config.py
```

---

## Steps

1. Implement provider adapter.
2. Keep prompt format consistent.
3. Handle authentication.
4. Add retry logic if appropriate.
5. Update configuration.

---

## Interface

```python
generate(prompt) -> structured_response
```

---

## Testing Checklist

- Authentication
- Response parsing
- Error handling
- Timeout handling

---

## Acceptance Criteria

- Existing prompts continue working.
- Structured output remains compatible.

---

# Adding a New Validator

Examples:

- Address validator
- Name similarity
- Date validator

## Files to Modify

```
layers/validation_layer.py
layers/confidence_layer.py
tests/
```

---

## Steps

1. Implement validation logic.
2. Return boolean or confidence contribution.
3. Update confidence weighting if required.
4. Add tests.

---

## Acceptance Criteria

- Validation output is deterministic.
- Confidence reasoning includes new validator.

---

# Adding a New Prompt

## Files

```
services/llm_service.py
```

---

## Steps

1. Add prompt template.
2. Preserve JSON output format.
3. Validate responses.
4. Test multiple examples.

---

## Acceptance Criteria

- Structured response remains stable.
- Existing APIs continue working.

---

# Adding a New Metric

Examples:

- OCR latency
- Validation duration
- Confidence distribution

## Files

```
layers/observability_layer.py
metrics/
```

---

## Steps

1. Register metric.
2. Record metric during execution.
3. Expose through `/metrics`.
4. Add tests.

---

## Acceptance Criteria

- Metric appears in endpoint.
- Metric collection has minimal performance impact.

---

# Adding a New Evaluation

Examples:

- New benchmark dataset
- Additional accuracy metric
- Domain-specific evaluation

## Files

```
evaluation/
benchmarking/
tests/
```

---

## Steps

1. Add evaluation dataset.
2. Implement evaluation script.
3. Generate benchmark report.
4. Document methodology.

---

## Acceptance Criteria

- Evaluation is reproducible.
- Reports are version controlled.

---

# Adding a New Capability

Examples:

- Fraud detection
- Signature verification
- Face verification

## Files

```
capabilities/
document_registry.py
sdk/
tests/
```

---

## Steps

1. Implement capability.
2. Register it.
3. Add SDK support if required.
4. Document behavior.
5. Add tests.

---

## Acceptance Criteria

- Capability is modular.
- Existing APIs remain compatible.

---

# Adding a New SDK Feature

## Files

```
sdk/
tests/test_sdk.py
README.md
```

---

## Steps

1. Extend SDK interface.
2. Maintain backward compatibility.
3. Update documentation.
4. Add unit tests.

---

## Acceptance Criteria

- Existing SDK users are unaffected.
- New feature is documented.

---

# Updating the API

Whenever API behavior changes:

1. Update request models.
2. Update response models.
3. Update Swagger documentation.
4. Update README.
5. Update REVIEW_PACKET.
6. Update tests.

---

# Extension Checklist

Before merging any extension, verify:

- [ ] Code follows layered architecture.
- [ ] No business logic added to API routes.
- [ ] Deterministic replay still functions.
- [ ] SDK remains backward compatible.
- [ ] Documentation updated.
- [ ] Unit tests added.
- [ ] Existing tests pass.
- [ ] Benchmark results reviewed (if applicable).

---

# Common Pitfalls

Avoid:

- Mixing responsibilities across layers.
- Skipping replay validation.
- Hardcoding provider-specific logic.
- Modifying ledger artifacts.
- Breaking SDK interfaces.
- Changing response formats without documentation.

---

# Review Guidelines

Every pull request introducing a new capability should answer:

- What problem does this solve?
- Which layer owns the change?
- Does replay remain deterministic?
- Are tests included?
- Has documentation been updated?
- Is backward compatibility preserved?

---

# Summary

The platform is designed to evolve through controlled, modular extensions. Future engineers should extend existing layers rather than bypassing them, maintain deterministic behavior, preserve backward compatibility, and ensure every new capability is accompanied by tests and documentation. Following this guide helps keep the platform maintainable, predictable, and consistent with the engineering standards established during the internship.