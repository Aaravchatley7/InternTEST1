# Accuracy Report

## Objective

Measure OCR and field extraction accuracy for Aadhaar and PAN document verification.

---

## Test Dataset

| Document Type | Samples |
| ------------- | ------- |
| Aadhaar       | 10      |
| PAN           | 10      |
| Total         | 20      |

---

## Aadhaar Extraction Results

| Metric              | Value |
| ------------------- | ----- |
| Total Samples       | 10    |
| Correct Extractions | 9     |
| Failed Extractions  | 1     |
| Accuracy            | 90%   |

### Common Failure Causes

* Low image quality
* Motion blur
* OCR character spacing issues

---

## PAN Extraction Results

| Metric              | Value |
| ------------------- | ----- |
| Total Samples       | 10    |
| Correct Extractions | 8     |
| Failed Extractions  | 2     |
| Accuracy            | 80%   |

### Common Failure Causes

* OCR confusion between similar characters
* Low contrast images
* Partial card captures

---

## Combined Results

| Metric              | Value |
| ------------------- | ----- |
| Total Samples       | 20    |
| Correct Extractions | 17    |
| Failed Extractions  | 3     |
| Overall Accuracy    | 85%   |

---

## Improvements Implemented

* EasyOCR integration
* Tesseract fallback support
* OCR preprocessing pipeline
* Aadhaar regex recovery
* PAN regex recovery
* LLM-assisted field extraction
* Extraction fallback logic
* Hybrid extraction architecture

---

## Conclusion

The system achieved an overall extraction accuracy of 85%, exceeding the minimum target of 80% specified in the sprint requirements.
