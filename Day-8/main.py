from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    stock: int


products = {
    1: {
        "id": 1,
        "name": "Laptop",
        "price": 75000,
        "stock": 10
    }
}


@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return products[product_id]


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED
)
def create_product(product: Product):

    new_id = max(products.keys()) + 1

    products[new_id] = {
        "id": new_id,
        **product.model_dump()
    }

    return products[new_id]


@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    del products[product_id]

    return {
        "message": "Product deleted"
    }