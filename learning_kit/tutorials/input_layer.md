# Input Layer Tutorial

## Purpose

The Input Layer validates incoming requests and uploaded files before processing begins.

## Inputs

- Aadhaar File
- PAN File
- User Form Data

## Outputs

- Validated Request

## Workflow

User Request

↓

File Validation

↓

Input Validation

↓

Extraction Layer

## Key File

layers/input_layer.py

## Extension Points

- Add new file types
- Add size validation
- Add MIME type validation