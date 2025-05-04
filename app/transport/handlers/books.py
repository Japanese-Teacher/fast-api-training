from typing import Annotated, Any, Coroutine

from fastapi import APIRouter, HTTPException, Depends

from app.integrations.postgres.book_repository import BookRepository
from app.models import Book
from app.services.book_service import BookService, get_book_service

book_router = APIRouter(
    prefix="/books",  # Префикс для всех эндпоинтов этого роутера
    tags=["Books"],  # Тег для группировки в документации Swagger
)


@book_router.get("", response_model=list[Book])
async def get_books(
        book_service: Annotated[BookService, Depends(BookService)]
) -> list[Book]:
    return book_service.get_books()


@book_router.post("", response_model=None)
async def add_book(
        book: Book,
        book_service: Annotated[BookService, Depends(BookService)],
) -> None:
    book_service.add_book(book)
    print(book_service)


@book_router.put("/{book_id}", response_model=Book)
async def update_book(
        book_id: int,
        book_service: Annotated[BookService, Depends(BookService)],
        new_book: str
) -> Book | None:
    try:
        return book_service.update_book(book_id, new_book)
    except ValueError:
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
