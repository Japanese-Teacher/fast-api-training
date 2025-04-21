from fastapi import APIRouter, HTTPException

from app.other import Book, books_db

book_router = APIRouter(
    prefix="/",  # Префикс для всех эндпоинтов этого роутера
    tags=["Books"],  # Тег для группировки в документации Swagger
)


@book_router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Добро пожаловать в API библиотеки!"}


@book_router.get("/books", response_model=list[Book])
async def get_books() -> list[Book]:
    return books_db


@book_router.post("/books", response_model=Book)
async def add_book(book: Book) -> Book:
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book)
    return book
