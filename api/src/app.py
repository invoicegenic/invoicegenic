'''
Aplication factory for the API

Functions:
    create_app(config: Config) -> Flask
    register_exts(app: Flask)
    register_bps(app: Flask)
'''
import extensions
from flask import Flask
from api.v0 import api_v0_bp
from config import config_by_env


def create_app() -> Flask:
    '''Create API app instance'''
    app = Flask(__name__)
    app.config.from_object(config_by_env[app.config['ENV']])

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


api_app = create_app()
