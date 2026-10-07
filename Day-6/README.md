# Day 6 — Request Body

## What I Learned

Today I learned how FastAPI receives JSON request bodies and validates them using Pydantic models.

## Topics Covered

- Request body
- JSON requests
- Pydantic request models
- Request validation
- Optional fields
- Nested request bodies
- Path + request body
- Query + request body
- Create vs update schemas

## Request Flow

```text
Client
  ↓
JSON Request
  ↓
FastAPI
  ↓
Pydantic
  ↓
Validation
  ↓
Python Object
  ↓
Route Function