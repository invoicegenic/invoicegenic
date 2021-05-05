'''
'''
import pytest
import pathlib
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


Base = declarative_base()


@pytest.fixture(scope='session')
def db_engine():
    try:
        fp = pathlib.Path().absolute().joinpath('.env.test')
        env = dotenv_values(str(fp))
    except RuntimeError as err:
        print(err)

    engine = create_engine(
        '{}+pymysql://{}:{}@{}:{}/{}'
        .format(env['DB_CONNECTION'], env['DB_USERNAME'], env['DB_PASSWORD'],
                env['DB_HOST'], env['DB_PORT'], env['DB_NAME'])
    )

    yield engine

    engine.dispose()


@pytest.fixture(scope='session')
def db_session_factory(db_engine):
    return scoped_session(sessionmaker(db_engine))


@pytest.fixture(scope='function')
def db_session(db_session_factory):
    session = db_session_factory()
    yield session

    session.rollback()
    session.close()


@pytest.fixture(scope='module', autouse=True)
def metadata(db_engine):
    '''Set up'''
    Base.metadata.create_all(db_engine)
    yield

    '''Tear down'''
    Base.metadata.drop_all(db_engine)
