from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from .routes import init_routes

    init_routes(app)

    return app
