'''
'''
import pytest
from sqlalchemy import Table, Column, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash

from lib import utc_now, to_mysql_datetime_string
from .conftest import Base

user_table = Table(
    'user',
    Base.metadata,
    Column('id', String(40), primary_key=True),
    Column('email', String(120), nullable=False, index=True, unique=True),
    Column('password', String(128), nullable=False),
    Column('created_at', DateTime, nullable=False, default=utc_now),
    Column('updated_at', DateTime, nullable=False,
           default=utc_now, onupdate=utc_now),
    Column('deleted_at', DateTime, nullable=True)
)

user_data = [dict(
    id='c2ac248d-e260-4c32-a8f6-e6c8bd41b359',
    email='test_1@invoicegenic.com',
    # password: 'test 1234'
    password='pbkdf2:sha256:120282$TAMiYaGN2oD86PQX9qee7iEZ7mwgfHI3$7d827291ff9d8c2c4c8b0dd5789994a861694edc3c9af72a802e7fbff4d12b9c',
)]


class User(Base):
    __table__ = user_table

    def __repr__(self):
        return f'<User {self.email}>'


@pytest.fixture
def get_user_from_db(db_session):
    return db_session.query(User).get('c2ac248d-e260-4c32-a8f6-e6c8bd41b359')


def test_user_create(db_session):
    for _, data in enumerate(user_data):
        user = User(id=data['id'], email=data['email'],
                    password=data['password'])
        db_session.add(user)

    db_session.commit()
    assert True


def test_user_get(db_session, get_user_from_db):
    user = get_user_from_db
    assert user is not None and user.id == 'c2ac248d-e260-4c32-a8f6-e6c8bd41b359'


def test_user_update(db_session, get_user_from_db):
    user = get_user_from_db
    new_email = 'test_1_new@invoicegenic.com'
    old_email = user.email

    user.email = new_email
    db_session.commit()

    user = get_user_from_db
    assert user.email == new_email


def test_user_delete(db_session, get_user_from_db):
    current_datetime = to_mysql_datetime_string(utc_now())
    user = get_user_from_db
    user.deleted_at = current_datetime
    db_session.commit()

    user = get_user_from_db
    assert user.deleted_at is not None and str(
        user.deleted_at) == current_datetime


def test_compare_plain_password_with_password_hash():
    plain = 'Undercut King Registrar7 Sandal'
    hash_method = 'pbkdf2:sha256:120282'
    salt_length = 32
    hash = generate_password_hash(plain, hash_method, salt_length)

    assert check_password_hash(hash, plain)
