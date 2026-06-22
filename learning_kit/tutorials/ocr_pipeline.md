# OCR Pipeline Tutorial

## Purpose

Extract text from uploaded identity documents.

## Inputs

- Image
- Document Scan

## Outputs

- OCR Text

## Workflow

Document

↓

Preprocessing

↓

EasyOCR

↓

Tesseract Fallback

↓

Extracted Text

## Files

services/ocr_service.py

layers/extraction_layer.py

## Extension Points

- Add Google Vision OCR
- Add AWS Textract
- Add Azure OCR