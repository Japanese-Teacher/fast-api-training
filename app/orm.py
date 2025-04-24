from mypyc.ir.ops import Integer
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

from app.models import books_db

# Формат строки подключения:
# postgresql://<username>:<password>@<host>:<port>/<database>
engine = create_engine('postgresql+psycopg2://user:password@localhost:5432/mydb')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Для проверки подключения


class BaseORM(DeclarativeBase):
    pass


class BookORM(BaseORM):
    def __repr__(self):
        return f"BookORM(id={self.id}, name={self.name})"
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

# BaseORM.metadata.create_all(bind=engine)
with SessionLocal() as session:
    query = select(BookORM).order_by(BookORM.name)
    print(session.execute(query).scalars().all())