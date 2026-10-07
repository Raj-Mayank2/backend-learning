from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class ProductCreate(BaseModel):
    name: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int


@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):

    return {
        "id": 1,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
        "internal_code": "PROD-001"
    }


@app.get("/products", response_model=list[ProductResponse])
def get_products():

    return [
        {
            "id": 1,
            "name": "Laptop",
            "price": 75000,
            "stock": 10
        },
        {
            "id": 2,
            "name": "Phone",
            "price": 40000,
            "stock": 20
        }
    ]