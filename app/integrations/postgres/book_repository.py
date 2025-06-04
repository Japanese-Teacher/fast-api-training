from typing import Annotated

from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models import BookDTO, AuthorDTO, NewBookDTO
from app.orm import BookORM, AuthorORM
from app.transport.depends.db import get_session

def paginate(query, page, size):
    offset_val = (page - 1) * size
    return query.offset(offset_val).limit(size)

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

    def get_books(
            self,
            page: int,
            size: int,
    ) -> list[BookDTO]:
        query = select(BookORM).order_by(BookORM.id)
        paginated_query = paginate(query, page, size)
        books_orm = self._session.execute(paginated_query)
        return [BookDTO(
            id=book_orm.id,
            authors=[
                AuthorDTO(
                    name=author_orm.name,
                    nationality=author_orm.nationality,
                    date_of_birth=author_orm.date_of_birth
                )
                for author_orm in book_orm.authors
            ],
            name=book_orm.name,
            publisher_name=book_orm.publisher_name,
            description=book_orm.description,
        )
            for book_orm in books_orm.scalars().all()
        ]

    def update_book(
            self,
            new_book_dto: NewBookDTO,
    ) -> NewBookDTO | None:
        book_orm = self._session.get(BookORM, new_book_dto.id)
        if book_orm:
            authors_orm = [
                AuthorORM(
                    name=author_dto.name,
                    nationality=author_dto.nationality,
                    date_of_birth=author_dto.date_of_birth,
                )
                for author_dto in new_book_dto.new_authors
            ]
            book_orm.name = new_book_dto.new_name
            book_orm.authors = authors_orm
            book_orm.description = new_book_dto.new_description
            book_orm.publisher_name = new_book_dto.new_publisher_name
            self._session.flush()
            self._session.refresh(book_orm)
        return new_book_dto
