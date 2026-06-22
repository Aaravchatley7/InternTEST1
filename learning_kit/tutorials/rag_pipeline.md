# RAG Pipeline Tutorial

## Purpose

Answer questions from uploaded PDF documents.

## Inputs

- PDF
- User Question

## Outputs

- Answer
- Confidence

## Workflow

PDF

↓

Chunking

↓

Embeddings

↓

FAISS

↓

Retrieval

↓

LLM

↓

Answer

## Files

layers/rag_layer.py

services/rag_service.py

services/vector_builder.py

## Extension Points

- Hybrid Search
- Re-ranking
- Multi-Document Retrieval