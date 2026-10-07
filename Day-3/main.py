from fastapi import FastAPI

app=FastAPI()


@app.get("/books")
def get_books():
    return{
        "message":"Getting all books"
    }

@app.get("/books/{book_id}")
def get_book(book_id):
    return{
        "book_id":book_id

    }

@app.get("/learn/{learn_id}")
def get_learn(learn_id:int):
    return{
        "learn_id":learn_id
    }


@app.get("/square/{number}")
def square(number:int):
    return{
        "number":number,
        "result":number*number
    }