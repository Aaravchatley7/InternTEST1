# Ecosystem Attachment Model

## Purpose

Define how BHIV capabilities attach to future products.

---

# Supported Attachment Modes

## Embedded

Capability runs inside consumer application.

Example:

```text
UniGuru
    ↓
Embedded BHIV SDK
```

---

## API Linked

Capability exposed through HTTP APIs.

Example:

```text
Consumer
    ↓
REST API
    ↓
BHIV
```

---

## Sidecar

Capability runs as independent service.

Example:

```text
Application
    ↓
BHIV Sidecar
```

---

## Reusable Capability

Capability imported directly.

Example:

```python
from sdk.verification_sdk import VerificationSDK
```