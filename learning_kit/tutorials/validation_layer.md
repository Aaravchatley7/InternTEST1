# Validation Layer Tutorial

## Purpose

Compare extracted document information against user-provided information.

## Inputs

- Form Data
- Extracted Identity Data

## Outputs

- Validation Results

## Workflow

Form Data

+

Identity Data

↓

Field Comparison

↓

Validation Decision

## File

layers/validation_layer.py

## Extension Points

- Add new validators
- Add fuzzy matching
- Add rule-based validation