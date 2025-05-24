from datetime import datetime

from mypyc.ir.ops import Integer
from sqlalchemy import create_engine, String, select, ForeignKey, text, Text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

from app.mixins import CreatedAtMixin, UpdatedAtMixin, DeletedAtMixin


class Base(DeclarativeBase):
    pass


class BaseORM(
    Base,
    CreatedAtMixin,
    UpdatedAtMixin,
    DeletedAtMixin,
):
    __abstract__ = True


class BookORM(BaseORM):
    def __repr__(self):
        return f"BookORM(id={self.id}, name={self.name}, description={self.description})"

    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    author_name: Mapped[str | None] = mapped_column(
        String(100),
        ForeignKey(
            "authors.name",
            ondelete="CASCADE",
        ),
    )
    publisher_name: Mapped[str] = mapped_column(
        String(100),
        ForeignKey("publishers.name"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(Text, default=None)


class AuthorORM(Base):
    def __repr__(self):
        return f"AuthorORM(name={self.name}, nationality={self.nationality})"

    __tablename__ = "authors"
    name: Mapped[str] = mapped_column(
        String(100),
        primary_key=True
    )
    date_of_birth: Mapped[datetime]
    nationality: Mapped[str] = mapped_column(String(50))


class UserORM(BaseORM):
    def __repr__(self):
        return f"UserORM(id={self.id}, login={self.login})"

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    second_name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    login: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)


class CommentORM(BaseORM):
    def __repr__(self):
        return f"CommentORM(id={self.id}, book_id={self.book_id})"

    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(
        ForeignKey(
            "books.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE", ),
        nullable=False,
    )
    comment: Mapped[str | None] = mapped_column(Text, default=None)


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
    review: Mapped[str] = mapped_column(Text, default=None)


class PublisherORM(Base):
    def __repr__(self):
        return f"PublisherORM(name={self.name})"

    __tablename__ = "publishers"

    name: Mapped[str] = mapped_column(String(100), primary_key=True)
