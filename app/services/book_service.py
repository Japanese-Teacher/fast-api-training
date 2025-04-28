from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.book_repository import BookRepository
from app.models import books_db


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

