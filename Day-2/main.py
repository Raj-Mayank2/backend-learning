from fastapi import FastAPI

app=FastAPI()


@app.get("/products")
def get_products():
    return {
        "message":"Getting all products"
    }


@app.post("/products")
def create_products():
    return{
        "message":"Product created"
    }


@app.put("/products")
def update_product():
    return{
        "message":"Product replaced"
    }

@app.patch("/products")
def patch_products():
    return{
        "message":"Product partially updated"
    }

@app.delete("/products")
def delete_products():
    return{
        "message":"Product deleted"
    }