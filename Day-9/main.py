
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Management API")


# 1. Models

class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


class BookUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float


# 2. Temporary in-memory storage

books = {
    1: {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 499.0,
    },
    2: {
        "id": 2,
        "title": "Deep Work",
        "author": "Cal Newport",
        "price": 399.0,
    },
    3: {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "price": 599.0,
    },
}

next_book_id = 4


# 3. GET all books, with search and pagination

@app.get("/books", response_model=list[BookResponse])
def get_books(
    search: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    result = list(books.values())

    if search:
        keyword = search.casefold()
        result = [
            book for book in result
            if keyword in book["title"].casefold()
            or keyword in book["author"].casefold()
        ]

    return result[skip:skip + limit]


# 4. GET one book

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    book = books.get(book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book


# 5. POST create a book

@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book: BookCreate):
    global next_book_id

    new_book = {
        "id": next_book_id,
        **book.model_dump(),
    }

    books[next_book_id] = new_book
    next_book_id += 1

    return new_book


# 6. PUT replace a book

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    updated_book = {
        "id": book_id,
        **book.model_dump(),
    }

    books[book_id] = updated_book
    return updated_book


# 7. DELETE a book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    del books[book_id]

    return {"message": "Book deleted successfully"}
