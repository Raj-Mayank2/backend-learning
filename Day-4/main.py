from fastapi import FastAPI


app=FastAPI()


products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics"
    },
    {
        "id": 2,
        "name": "Phone",
        "category": "electronics"
    },
    {
        "id": 3,
        "name": "Desk",
        "category": "furniture"
    },
    {
        "id": 4,
        "name": "Chair",
        "category": "furniture"
    }
]

@app.get("/products")
def get_products(category: str = ""):

    if category:
        filtered_products = [
            product
            for product in products
            if product["category"] == category
        ]
    else:
        filtered_products = products

    return {
        "products": filtered_products
    }


@app.get("/products/{product_id}")
def get_product(
    product_id:int,
    include_reviews:bool=False
):
    return{
        "product_id":product_id,
        "include_reviews":include_reviews
    }

