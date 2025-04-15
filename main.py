from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str


books_db = [
    Book(id=1, title = "Sample Book", author= "Sample Author")
]

@app.get("/books", response_model=List[Book])
async def get_books():
    return books_db

@app.post("/books", response_model=Book)
async def add_book(book: Book):

    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book)
    return book