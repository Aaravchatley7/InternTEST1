# Architecture Summary

The platform follows a layered architecture:

Input

↓

OCR

↓

Extraction

↓

Validation

↓

Confidence

↓

Evidence

↓

Observability

↓

Provenance

↓

Ledger

↓

Replay

↓

SDK

↓

Consumer

Each layer owns a single responsibility, making the platform modular, testable, and extensible.