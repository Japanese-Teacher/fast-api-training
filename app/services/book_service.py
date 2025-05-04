from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.book_repository import BookRepository
from app.models import Book


# from app.models import books_db


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

    def add_book(self, book: Book) -> Book:
        print("add_book worked")
        return self._book_repository.add_book(book)

    def get_books(self) -> list[Book]:
        return self._book_repository.get_books()

    def update_book(
            self,
            book_id: int,
            new_data: str
    ) -> None:
        print("update_book worked")
        return self._book_repository.update_book(book_id, new_data)


def get_book_service():
    return None
