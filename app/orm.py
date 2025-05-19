from datetime import datetime

from mypyc.ir.ops import Integer
from sqlalchemy import create_engine, String, select, ForeignKey, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


class BaseORM(DeclarativeBase):
    pass


class BookORM(BaseORM):
    def __repr__(self):
        return f"BookORM(id={self.id}, name={self.name}, description={self.description})"

    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    author_name: Mapped[str] = mapped_column(ForeignKey("authors.name", ondelete="CASCADE"), nullable=False)
    publisher_name: Mapped[str] = mapped_column(ForeignKey("publishers.name"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True, default=None)
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=False)
    deleted_at: Mapped[datetime | None] = mapped_column(nullable=True)


class AuthorORM(BaseORM):
    def __repr__(self):
        return f"AuthorORM(name={self.name}, nationality={self.nationality})"

    __tablename__ = "authors"
    name: Mapped[str] = mapped_column(primary_key=True)
    date_of_birth: Mapped[datetime] = mapped_column(nullable=True)
    nationality: Mapped[str] = mapped_column(nullable=True)


class UserORM(BaseORM):
    def __repr__(self):
        return f"UserORM(id={self.id}, login={self.login})"

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    second_name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"), onupdate=text("now()"))
    deleted_at: Mapped[datetime] = mapped_column(nullable=True)


class CommentORM(BaseORM):
    def __repr__(self):
        return f"CommentORM(id={self.id}, book_id={self.book_id})"

    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    comment: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"), onupdate=text("now()"))
    deleted_at: Mapped[datetime | None] = mapped_column(nullable=True)


class ReadingRelationORM(BaseORM):
    def __repr__(self):
        return f"ReadingRelationORM(book_id={self.book_id}, user_id={self.user_id})"

    __tablename__ = "reading_relation"

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id",
                   ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    continue_page: Mapped[int] = mapped_column(nullable=False, default=0)
    favourite: Mapped[bool] = mapped_column(nullable=False, default=False)
    review: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"), onupdate=text("now()"))
    deleted_at: Mapped[datetime | None] = mapped_column(nullable=True)
