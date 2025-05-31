from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.publisher_repository import PublisherRepository
from app.models import PublisherDTO


class PublisherService:
    def __init__(
            self,
            publisher_repository: Annotated[PublisherRepository, Depends(PublisherRepository)],
    ):
        self.publisher_repository = publisher_repository

    def get_publishers(self) -> list[PublisherDTO]:
        return self.publisher_repository.get_publishers()

    def add_publisher(
            self,
            publisher_dto: PublisherDTO,
    ) -> PublisherDTO:
        return self.publisher_repository.add_publisher(publisher_dto)
