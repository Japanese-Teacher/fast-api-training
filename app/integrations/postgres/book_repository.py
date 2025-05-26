from typing import Annotated

from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models import BookDTO, AuthorDTO
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
        self._session.flush()

    def add_book(
            self,
            book: BookDTO
    ) -> None:
        self._session.add(
            BookORM(
                id=book.id,
                name=book.name,
                publisher_name=book.publisher_name,
                description=book.description,
            )
        )
        self._session.flush()

    def get_books(self) -> list[BookDTO]:
        query_result = self._session.execute(select(BookORM))
        result = []
        for book_orm in query_result.scalars().all():
            authors_dto = []
            for author_orm in book_orm.authors:
                author_dto = AuthorDTO(
                    name=author_orm.name,
                    nationality=author_orm.nationality,
                    date_of_birth=author_orm.date_of_birth
                )
                authors_dto.append(author_dto)
            result.append(
                BookDTO(
                    id=book_orm.id,
                    authors=authors_dto,
                    name=book_orm.name,
                    publisher_name=book_orm.publisher_name,
                    description=book_orm.description,
                )
            )
        return result

    def update_book(
            self,
            book_id: int,
            new_name:str,
            new_publisher_name: str,
            new_description: str,
    ) -> BookDTO | None:
        book = self._session.get(BookORM, book_id)
        if book:
            book.name = new_name
            book.publisher_name = new_publisher_name
            book.description = new_description
            self._session.flush()
            self._session.refresh(book)
        return book
