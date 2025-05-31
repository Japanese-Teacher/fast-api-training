from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import AuthorDTO
from app.services.author_service import AuthorService

author_router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)

@author_router.get('', response_model=list[AuthorDTO])
async def get_authors(
        author_service: Annotated[AuthorService, Depends(AuthorService)]
) -> list[AuthorDTO]:
    result = author_service.get_authors()
    return result
