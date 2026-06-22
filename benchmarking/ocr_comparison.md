# OCR Quality Comparison

## OCR Engines

### EasyOCR

Advantages:

- Better multilingual support
- Strong document recognition
- Good Aadhaar extraction

Limitations:

- Slower than Tesseract

---

### Tesseract

Advantages:

- Lightweight
- Fast

Limitations:

- More OCR noise
- Lower extraction quality on low-resolution documents

---

## Current Strategy

Primary:

EasyOCR

Fallback:

Tesseract

---

## Future Benchmarking

Compare:

- Extraction Accuracy
- Processing Latency
- OCR Noise Tolerance
- Document Coverage