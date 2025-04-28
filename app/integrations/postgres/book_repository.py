from typing import Annotated

from fastapi import Depends
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.orm import BookORM
from app.transport.depends.db import get_session


class BookRepository:
    def __init__(
        self,
        session: Annotated[Session, Depends(get_session)],
    ):
        self._session = session

    def delete_book(self, book_id: int) -> None:
        self._session.execute(delete(BookORM).where(BookORM.id == book_id))