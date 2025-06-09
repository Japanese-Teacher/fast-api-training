from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.integrations.postgres.book_repository import paginate
from app.models import AuthorDTO, NewAuthorDTO
from app.orm import AuthorORM
from app.transport.depends.db import get_session


class AuthorRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)],
    ):
        self._session = session

    def get_authors(
            self,
            page: int,
            size: int
    ) -> list[AuthorDTO]:
        query = select(AuthorORM)
        paginated_query = paginate(query, page, size)
        authors_orm = self._session.execute(paginated_query)
        return [AuthorDTO(
            name=author_orm.name,
            nationality=author_orm.nationality,
            date_of_birth=author_orm.date_of_birth,
        )
        for author_orm in authors_orm.scalars().all()
    ]


    def add_author(
            self,
            author_dto: AuthorDTO
    ) -> AuthorDTO:
        self._session.add(
            AuthorORM(
                name=author_dto.name,
                nationality=author_dto.nationality,
                date_of_birth=author_dto.date_of_birth,
            )
        )
        self._session.flush()
        return author_dto

    def update_author(
            self,
            author_name: str,
            new_author_dto: NewAuthorDTO,
    ) -> NewAuthorDTO:
        new_author_orm = self._session.get(AuthorORM, author_name)
        if new_author_orm:
            new_author_orm.name = new_author_dto.new_name
            new_author_orm.nationality = new_author_dto.new_nationality
            new_author_orm.date_of_birth = new_author_dto.new_date_of_birth
            self._session.flush()
            self._session.refresh(new_author_orm)
        return new_author_dto
    def delete_author(
            self,
            author_name: str,
    ) -> str:
        self._session.execute(delete(AuthorORM).where(AuthorORM.name == author_name))
        self._session.flush()
        return "Удаление успешно произведено"