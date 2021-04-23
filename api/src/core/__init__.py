'''Core module'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(app_config):
    '''Create app function'''
    app = Flask(__name__)
    app.config.from_object(app_config)

    from api.v0 import bp as api_v0_bp
    app.register_blueprint(api_v0_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    from core import models

    return app
