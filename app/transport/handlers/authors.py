from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import AuthorDTO, NewAuthorDTO
from app.services.author_service import AuthorService

author_router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)


@author_router.get('', response_model=list[AuthorDTO])
async def get_authors(
        author_service: Annotated[AuthorService, Depends(AuthorService)]
) -> list[AuthorDTO]:
    return author_service.get_authors()


@author_router.post('', response_model=AuthorDTO)
async def add_author(
        author_service: Annotated[AuthorService, Depends(AuthorService)],
        author_dto: AuthorDTO
) -> AuthorDTO:
    return author_service.add_author(author_dto)


@author_router.put('', response_model=NewAuthorDTO)
async def update_author(
        author_service: Annotated[AuthorService, Depends(AuthorService)],
        author_name: str,
        new_author_dto: NewAuthorDTO,
) -> NewAuthorDTO:
    return author_service.update_author(author_name, new_author_dto)


@author_router.delete('', response_model=str)
async def delete_author(
        author_service: Annotated[AuthorService, Depends(AuthorService)],
        author_name: str,
) -> str:
    return author_service.delete_author(author_name)
