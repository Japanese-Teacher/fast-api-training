from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from app.models import BookDTO, NewBookDTO
from app.services.book_service import BookService

book_router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@book_router.get("", response_model=list[BookDTO])
async def get_books(
        book_service: Annotated[BookService, Depends(BookService)]
) -> list[BookDTO]:
    result = book_service.get_books()
    return result

@book_router.post("", response_model=None)
async def add_book(
        book: BookDTO,
        book_service: Annotated[BookService, Depends(BookService)],
) -> None:
    book_service.add_book(book)


@book_router.put("/{book_id}", response_model=NewBookDTO)
async def update_book(
        book_service: Annotated[BookService, Depends(BookService)],
        new_book_dto: NewBookDTO
) -> NewBookDTO | None:
    try:
        return book_service.update_book(
            new_book_dto
        )
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
