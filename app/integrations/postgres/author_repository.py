from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import AuthorDTO
from app.orm import AuthorORM
from app.transport.depends.db import get_session


class AuthorRepository:
    def __init__(
            self,
            session = Annotated[Session, Depends(get_session)],
    ):
        self._session = session
    def get_authors(self) -> list[AuthorDTO]:
        query_result = self._session.execute(select(AuthorORM))
        authors_dto = []
        for author_orm in query_result.scalars().all():
            author_dto = AuthorDTO(
                name=author_orm.name,
                nationality=author_orm.nationality,
                date_of_birth=author_orm.date_of_birth,
            )
            authors_dto.append(author_dto)
        return authors_dto
