# Day 10 — Student Management System

## Overview

A modular REST API built with FastAPI for managing student records. This project introduces clean folder organization and route separation using `APIRouter`.

## Features

- Create, list, retrieve, update, and delete students
- Search students by name or email
- Filter students by course
- Pagination with `skip` and `limit`
- Request validation using Pydantic
- HTTP error handling for missing students
- Separate request and response schemas
- Health check endpoint

## Project Structure

```text
app/
├── main.py
├── schemas/
│   └── student.py
├── routers/
│   └── students.py
└── data/
    └── student_store.py
```

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/students/` | List and filter students |
| GET | `/students/{student_id}` | Retrieve a student |
| POST | `/students/` | Create a student |
| PUT | `/students/{student_id}` | Replace student data |
| PATCH | `/students/{student_id}` | Partially update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Run Locally

```bash
pip install fastapi uvicorn
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API.

## Concepts Learned

- `APIRouter` and `include_router()`
- Route prefixes and Swagger tags
- Modular FastAPI applications
- Pydantic request and response schemas
- CRUD operations
- Search, filtering, and pagination
- `HTTPException` and status codes
- Partial updates with `model_dump(exclude_unset=True)`

## Limitations

The application uses in-memory storage. Data is not persistent and is lost when the server restarts. The storage layer will be replaced with a database in a future module.

## Next Steps

Learn dependency injection with `Depends()` and reusable dependencies.
