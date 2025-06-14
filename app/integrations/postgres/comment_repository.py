from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.integrations.postgres.book_repository import paginate
from app.models import CommentDTO
from app.orm import CommentORM
from app.transport.depends.db import get_session


class CommentRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)],
    ):
        self._session = session

    def get_comments(
            self,
            book_id: int,
            page: int,
            size: int
    ) -> list[CommentDTO]:
        query = select(CommentORM).where(CommentORM.book_id == book_id)
        paginated_query = paginate(query, page, size)
        comments_orm = self._session.execute(paginated_query)
        return [
            CommentDTO(
                id=comment_orm.id,
                book_id=comment_orm.book_id,
                user_id=comment_orm.user_id,
                comment=comment_orm.comment,
            )
            for comment_orm in comments_orm.scalars().all()
        ]

    def add_comment(
            self,
            comment_dto: CommentDTO,
    ) -> CommentDTO:
        self._session.add(
            CommentORM(
                id=comment_dto.id,
                book_id=comment_dto.id,
                user_id=comment_dto.user_id,
                comment=comment_dto.comment
            )
        )
        self._session.flush()
        return comment_dto

    def update_comment(
            self,
            comment_id: int,
            new_comment: str,
    ) -> str:
        comment_orm = self._session.get(CommentORM, comment_id)
        if comment_orm:
            comment_orm.comment = new_comment
            self._session.flush()
            self._session.refresh(comment_orm)
        return new_comment

    def delete_comment(
            self,
            comment_id: int
    ) -> str:
        self._session.execute(delete(CommentORM).where(CommentORM.id == comment_id))
        return "Удаление успешно произведено"
