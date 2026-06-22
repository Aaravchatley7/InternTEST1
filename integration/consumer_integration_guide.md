# Consumer Integration Guide

## Objective

Help future teams consume BHIV capabilities.

---

# Step 1

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 2

Configure Environment

```env
OPENROUTER_API_KEY=your_key
```

---

# Step 3

Use SDK

```python
from sdk.verification_sdk import VerificationSDK

sdk = VerificationSDK()

result = sdk.verify(
    form_data,
    document_path,
    document_type
)
```

---

# Step 4

Consume Results

Returned:

- Validation
- Confidence
- Evidence

---

# Step 5

Optional Replay

```http
GET /replay/{trace_id}
```

---

# Recommended Integration Pattern

```text
Consumer
    ↓
SDK/API
    ↓
BHIV Capability
    ↓
Validation + Confidence + Evidence
```