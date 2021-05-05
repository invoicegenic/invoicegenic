'''
'''


def db_setting(env_vars: dict) -> dict:
    return dict(
        SQLALCHEMY_DATABASE_URI=_db_uri_string(**env_vars),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )


def _db_uri_string(DB_CONNECTION: str = 'mysql',
                   DB_USERNAME: str = 'root',
                   DB_PASSWORD: str = '',
                   DB_HOST: str = 'localhost',
                   DB_PORT: str = '3306',
                   DB_NAME: str = '',
                   **kwargs) -> str:
    return '{}+pymysql://{}:{}@{}:{}/{}' \
        .format(DB_CONNECTION, DB_USERNAME, DB_PASSWORD,
                DB_HOST, DB_PORT, DB_NAME)
