from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.author_repository import AuthorRepository
from app.models import AuthorDTO, NewAuthorDTO


class AuthorService:
    def __init__(
            self,
            author_repository: Annotated[AuthorRepository, Depends(AuthorRepository)]
    ):
        self.author_repository = author_repository

    def get_authors(self) -> list[AuthorDTO]:
        return self.author_repository.get_authors()

    def add_author(
            self,
            author_dto: AuthorDTO,
    ) -> AuthorDTO:
        return self.author_repository.add_author(author_dto)

    def update_author(
            self,
            author_name: str,
            new_author_dto: NewAuthorDTO,
    ) -> NewAuthorDTO:
        return self.author_repository.update_author(author_name, new_author_dto)

    def delete_author(
            self,
            author_name: str,
    ) -> str:
        return self.author_repository.delete_author(author_name)

