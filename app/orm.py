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
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"), nullable = False)
    updated_at: Mapped[datetime] = mapped_column(nullable = False)
    deleted_at: Mapped[datetime | None] = mapped_column(nullable = True)