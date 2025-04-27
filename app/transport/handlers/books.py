from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from app.models import Book, books_db
from app.services.book_service import BookService, get_book_service, get_a, get_b

book_router = APIRouter(
    prefix="/books",  # Префикс для всех эндпоинтов этого роутера
    tags=["Books"],  # Тег для группировки в документации Swagger
)


@book_router.get("", response_model=list[Book])
async def get_books() -> list[Book]:
    return books_db


@book_router.post("", response_model=Book)
async def add_book(book: Book) -> Book:
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book)
    return book


@book_router.put("/{book_id}", response_model=Book)
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

@book_router.delete("/{book_id}", response_model=dict)
async def delete_book(
    book_service: Annotated[BookService, Depends(BookService)],
    book_id: int,
) -> dict[str, str]:
    try:
        book_service.delete_book(book_id)
        return {"message": "Книга успешно удалена"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Книга не найдена")
