from fastapi import FastAPI
from pydantic import BaseModel,Field


app=FastAPI()


class Address(BaseModel):
    city:str
    state:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address


@app.post("/users")
def create_user(user:User):
    return{
        "name":user.name,
        "age":user.age,
        "email":user.email,
        "address":user.address
    }


class Product(BaseModel):
    name:str
    price:float=Field(gt=0)
    stock:int=Field(ge=0)

@app.post("/products")
def create_product(product:Product):
    return{
        "message":"Product created",
        "product":product
    }
