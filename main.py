from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str


books_db = [
    Book(id=1, title="Sample Book", author="Sample Author")
]

@app.get("/")
async def root() -> dict:
    return {"message": "Добро пожаловать в API библиотеки!"}

@app.get("/books", response_model=list[Book])
async def get_books() -> list:
    return books_db

@app.post("/books", response_model=Book)
async def add_book(book: Book) -> Book:

    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book)
    return book