import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing import fixture

from app.orm import Base


@fixture(scope='session')
def engine():
    return create_engine(os.getenv("TEST_DB"))

@fixture(scope='session', autouse =True)
def create_db(engine):
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@fixture
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    session_making = sessionmaker(bind=connection)
    session = session_making()
    yield session
    session.close()
    transaction.rollback()
    connection.close()