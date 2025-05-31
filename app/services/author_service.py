from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.author_repository import AuthorRepository
from app.models import AuthorDTO


class AuthorService:
    def __init__(
            self,
            author_repository: Annotated[AuthorRepository, Depends(AuthorRepository)]
    ):
        self.author_repository = author_repository

    def get_authors(self) -> list[AuthorDTO]:
        return self.author_repository.get_authors()
