from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import CommentDTO
from app.services.comment_service import CommentService

comment_router = APIRouter(
    prefix='/comments',
    tags=['Comments']
)


@comment_router.get('', response_model=list[CommentDTO])
async def get_comments(
        comment_service: Annotated[CommentService, Depends(CommentService)],
        book_id: int,
        page: int,
        size: int,
) -> list[CommentDTO]:
    return comment_service.get_comments(book_id. page, size)


@comment_router.post('', response_model=CommentDTO)
async def add_comment(
        comment_service: Annotated[CommentService, Depends(CommentService)],
        comment_dto: CommentDTO
) -> CommentDTO:
    return comment_service.add_comment(comment_dto)


@comment_router.put('', response_model=str)
async def update_comment(
        comment_service: Annotated[CommentService, Depends(CommentService)],
        comment_id: int,
        new_comment: str,
) -> str:
    return comment_service.update_comment(comment_id, new_comment)


@comment_router.delete('', response_model=str)
async def delete_comment(
        comment_service: Annotated[CommentService, Depends(CommentService)],
        comment_id: int
) -> str:
    return comment_service.delete_comment(comment_id)
