from typing import Annotated

from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models import BookDTO
from app.orm import BookORM
from app.transport.depends.db import get_session


class BookRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)],
    ):
        self._session = session

    def delete_book(self, book_id: int) -> None:
        self._session.execute(delete(BookORM).where(BookORM.id == book_id))
        self._session.commit()

    def add_book(
            self,
            book: BookDTO
    ) -> None:
        self._session.add(
            BookORM(
                id=book.id,
                name=book.name,
            )
        )
        self._session.commit()

    def get_books(self) -> list[BookDTO]:
        query_result = self._session.execute(select(BookORM))
        result = []
        for book in query_result.scalars().all():
            result.append(
                BookDTO(
                    id=book.id,
                    name=book.name,
                )
            )
        return result

    def update_book(
            self,
            book_id: int,
            new_data: str,
    ) -> BookDTO | None:
        book = self._session.get(BookORM, book_id)
        if book:
            book.name = new_data
            self._session.commit()
            self._session.refresh(book)
        return book
