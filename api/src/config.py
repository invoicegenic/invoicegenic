'''
API configuration object

Classes:
    Config
    DevConfig
    ProdConfig

Functions:
    apply_config(env: string) -> Config
'''
from os import environ as env


class Config(object):
    '''Class that represents common base config'''
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


class DevConfig(Config):
    '''
    Class that represents config when API run in development environment.
    This class extends the base config.
    '''
    pass


class ProdConfig(Config):
    '''
    Class that represents config when API run in production environment.
    This class extends the base config.
    '''
    pass


# TODO Create TestConfig class

# TODO Return another config for TestConfig
config_by_env = dict(
    development=DevConfig,
    production=ProdConfig
)
