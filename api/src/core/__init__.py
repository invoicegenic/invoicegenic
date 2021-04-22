from flask import Flask


def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from api.v0 import bp as api_v0_bp
    app.register_blueprint(api_v0_bp)

    return app
