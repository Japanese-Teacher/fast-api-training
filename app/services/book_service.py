from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.book_repository import BookRepository
from app.models import BookDTO, NewBookDTO


class BookService:
    def __init__(
            self,
            book_repository: Annotated[BookRepository, Depends(BookRepository)],
    ):
        self._book_repository = book_repository

    def delete_book(
            self,
            book_id: int,
    ) -> None:
        return self._book_repository.delete_book(book_id)

    def add_book(self, book: BookDTO) -> None:
        return self._book_repository.add_book(book)

    def get_books(
            self,
            page: int,
            size: int,
    ) -> list[BookDTO]:
        return self._book_repository.get_books(page, size)

    def update_book(
            self,
            new_book_dto: NewBookDTO,
    ) -> None:
        return self._book_repository.update_book(
            new_book_dto,
        )


def get_book_service():
    return None
