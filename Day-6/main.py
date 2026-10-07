from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

class Product(BaseModel):
    name:str
    price:float
    stock:int

@app.post("/products")
def create_product(product:Product):
    return product


class StudentCreate(BaseModel):
    name:str
    result:float=Field(gt=0)
    age:int=Field(ge=0)
    description:str | None=None

@app.post("/students")
def create_student(student:StudentCreate):
    return{
        "message":"Student created successfully",
        "student":student
    }