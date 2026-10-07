# Day 5 — Pydantic Models

## What I Learned

Today I learned how Pydantic models provide structured data validation for FastAPI applications.

## Topics Covered

- BaseModel
- Type validation
- Required fields
- Default values
- Optional fields
- Nested models
- Lists
- Lists of models
- Field constraints
- model_dump()

## Example

```python
class Product(BaseModel):
    name: str
    price: float
    stock: int