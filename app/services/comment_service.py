from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.comment_repository import CommentRepository
from app.models import CommentDTO


class CommentService:
    def __init__(
            self,
            comment_repository: Annotated[CommentRepository, Depends(CommentRepository)],
    ):
        self.comment_repository = comment_repository

    def get_comments(
            self,
            book_id: int,
            page: int,
            size: int,
    ) -> list[CommentDTO]:
        return self.comment_repository.get_comments(book_id, page, size)

    def add_comment(
            self,
            comment_dto: CommentDTO,
    ) -> CommentDTO:
        return self.comment_repository.add_comment(comment_dto)

    def update_comment(
            self,
            comment_id: int,
            new_comment: str,
    ) -> str:
        return self.comment_repository.update_comment(comment_id, new_comment)

    def delete_comment(
            self,
            comment_id: int
    ) -> str:
        return self.comment_repository.delete_comment(comment_id)
