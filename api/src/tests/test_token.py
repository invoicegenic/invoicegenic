'''
'''
import jwt
import time
import pytest
from os import urandom
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

from lib import utc_now, to_timestamp


secret = urandom(24)

user_data = dict(
    id='c2ac248d-e260-4c32-a8f6-e6c8bd41b359',
    # email=None,
    # password=None
)

token = None


@pytest.fixture
def create_encoded_jwt():
    payload = {
        'sub': user_data['id'],
        'exp': utc_now() + timedelta(seconds=2)
    }
    yield jwt.encode(payload, secret, algorithm='HS256')


@pytest.fixture
def jwt_args():
    return dict(
        algorithms=['HS256'],
        options=dict(
            require=['sub', 'exp'],
            verify_exp=True
        )
    )


def test_create_jwt(create_encoded_jwt):
    global token
    token = create_encoded_jwt
    assert isinstance(token, (str, bytes))


def test_sub_and_exp_are_in_claim(jwt_args):
    decoded = jwt.decode(token, secret, **jwt_args)
    assert 'sub' in decoded and 'exp' in decoded \
        and decoded['sub'] == user_data['id']


def test_jwt_is_not_expired(jwt_args):
    time.sleep(1)
    try:
        decoded = jwt.decode(token, secret, **jwt_args)
    except:
        raise jwt.exceptions.ExpiredSignatureError
    finally:
        assert True


def test_renew_jwt(create_encoded_jwt, jwt_args):
    global token
    old_token = token
    old_claim = jwt.decode(old_token, secret, **jwt_args)
    token = create_encoded_jwt
    claim = jwt.decode(token, secret, **jwt_args)
    assert old_token != token \
        and to_timestamp(utc_now()) < int(claim['exp'])


def test_jwt_is_expired(jwt_args):
    time.sleep(3)
    with pytest.raises(jwt.exceptions.ExpiredSignatureError):
        decoded = jwt.decode(token, secret, **jwt_args)
