from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.models import PublisherDTO, NewPublisherDTO
from app.orm import PublisherORM
from app.transport.depends.db import get_session


class PublisherRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)],
    ):
        self._session = session

    def get_publishers(
            self,
            page: int,
            size: int,
    ) -> list[PublisherDTO]:
        offset_val = (page - 1) * size
        publishers_orm = self._session.execute(
            select(PublisherORM)
            .offset(offset_val)
            .limit(size)
        )
        return [PublisherDTO(
            name=publisher_orm.name,
        )
            for publisher_orm in publishers_orm.scalars().all()
        ]

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

    def update_publisher(
            self,
            publisher_name: str,
            new_publisher_dto: NewPublisherDTO,
    ) -> NewPublisherDTO:
        publisher_orm = self._session.get(PublisherORM, publisher_name)
        if publisher_orm:
            publisher_orm.name = new_publisher_dto.name
            self._session.flush()
            self._session.refresh(publisher_orm)
        return new_publisher_dto

    def delete_publisher(
            self,
            publisher_name: str,
    ) -> str:
        self._session.execute(delete(PublisherORM).where(PublisherORM.name == publisher_name))
        return "Удаление успешно произведено"
