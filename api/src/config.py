'''Config module'''
from os import environ as env


class Config(object):
    '''Config class'''
    SQLALCHEMY_DATABASE_URI = '{}+pymysql://{}:{}@{}:{}/{}' \
        .format(
            env.get('DB_CONNECTION'),
            env.get('DB_USERNAME'),
            env.get('DB_PASSWORD') or '',
            env.get('DB_HOST'),
            env.get('DB_PORT') or '3306',
            env.get('DB_NAME')
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
