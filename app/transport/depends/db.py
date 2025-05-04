from typing import Generator, Annotated

from fastapi import Depends
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


def get_engine() -> Engine:
    return create_engine('postgresql+psycopg2://user:password@localhost:5432/mydb')


def get_session_maker(
    engine: Annotated[Engine, Depends(get_engine)]
) -> sessionmaker:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session(
    session_maker: Annotated[sessionmaker, Depends(get_session_maker)],
) -> Generator[Session, None, None]:
    with session_maker() as session:
        yield session