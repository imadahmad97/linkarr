from flask import Flask
import logging
from .config import Config


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    app.logger.info("Loading configuration")
    app.config.from_object(Config)

    from .routes import init_routes

    app.logger.info("Initializing routes")
    init_routes(app)

    app.logger.info("Flask app initialized")
    return app
