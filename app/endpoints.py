from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.models import Book, books_db
from app.orm import SessionLocal, BookORM

book_router = APIRouter(
    prefix="",  # Префикс для всех эндпоинтов этого роутера
    tags=["Books"],  # Тег для группировки в документации Swagger
)


@book_router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Добро пожаловать в API библиотеки!"}


@book_router.get("/books", response_model=list[Book])
async def get_books() -> list[Book]:
    with SessionLocal() as session:
        query = select(BookORM).order_by(BookORM.name)
        query_result = session.execute(query).scalars().all()
        return [
            Book(
                id=book.id,
                title=book.name,
            )
            for book in query_result
        ]


@book_router.post("/books", response_model=Book)
async def add_book(book: Book) -> Book:
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book)
    return book


@book_router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book) -> Book:
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            if updated_book.id != book_id:
                for b in books_db:
                    if b.id == updated_book.id and b.id != book_id:
                        raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")

            books_db[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@book_router.delete("/books/{book_id}", response_model=dict)
async def delete_book(book_id: int) -> dict[str, str | Book]:
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            deleted_book = books_db.pop(idx)
            return {"message": "Книга успешно удалена", "deleted_book": deleted_book}
    raise HTTPException(status_code=404, detail="Книга не найдена")