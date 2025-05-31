from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import PublisherDTO
from app.orm import PublisherORM
from app.transport.depends.db import get_session


class PublisherRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)],
    ):
        self._session = session

    def get_publishers(self) -> list[PublisherDTO]:
        publishers_orm = self._session.execute(select(PublisherORM))
        publishers_dto = []
        for publisher_orm in publishers_orm.scalars().all():
            publisher_dto = PublisherDTO(
                name=publisher_orm.name,
            )
            publishers_dto.append(publisher_dto)
        return publishers_dto

    def add_publisher(
            self,
            publisher_dto: PublisherDTO,
    ) -> PublisherDTO:
        self._session.add(
            PublisherORM(
                name=publisher_dto.name,
            )
        )
        self._session.flush()
        return publisher_dto
