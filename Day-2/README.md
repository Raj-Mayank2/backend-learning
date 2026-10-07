# Day 2 — HTTP Methods & REST APIs

## What I Learned

Today I learned the main HTTP methods used when building REST APIs with FastAPI.

## HTTP Methods

| Method | Purpose |
|---|---|
| GET | Read data |
| POST | Create data |
| PUT | Replace/update data |
| PATCH | Partially update data |
| DELETE | Delete data |

## CRUD

- Create → POST
- Read → GET
- Update → PUT/PATCH
- Delete → DELETE

## Project

Built a basic Product API with:

- GET /products
- POST /products
- PUT /products
- PATCH /products
- DELETE /products

## Running the Project

```bash
uvicorn main:app --reload