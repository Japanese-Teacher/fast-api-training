from mypyc.ir.ops import Integer
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


class BaseORM(DeclarativeBase):
    pass


class BookORM(BaseORM):
    def __repr__(self):
        return f"BookORM(id={self.id}, name={self.name})"

    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
