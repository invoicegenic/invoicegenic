'''
Aplication factory for the API

Functions:
    create_app() -> Flask
    register_exts(app: Flask)
    register_bps(app: Flask)
    configure_app(env: str, run_as_test: bool = False) -> dict
'''
import pathlib
from flask import Flask
from dotenv import dotenv_values

import extensions
from api.v0 import api_v0_bp
from settings.db import db_setting


def create_app(use_test_env: bool = False) -> Flask:
    '''Create API app instance'''
    app = Flask(__name__)
    app.config.update(
        configure_app(app.config['ENV'], use_test_env)
    )

    register_exts(app)
    register_bps(app)

    return app


def register_exts(app: Flask):
    '''Register API extensions'''
    extensions.db.init_app(app)
    extensions.migrate.init_app(app, extensions.db)


def register_bps(app: Flask):
    '''Register API blueprints'''
    app.register_blueprint(api_v0_bp)


def configure_app(env: str, run_as_test: bool) -> dict:
    '''Configure API app settings'''
    if env == 'development' and run_as_test:
        env = 'test'

    env_vars = dotenv_values(str(
        pathlib.Path().absolute().joinpath(f'.env.{env}')
    ))

    settings = dict(**db_setting(env_vars))
    if run_as_test:
        settings['TESTING'] = True

    return settings


api_app = create_app()
