from flask import Flask
import logging
from .model.config import Config


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    app.logger.info("Loading flask configurations")
    app.config.from_object(Config)
    app.logger.info("Flask configurations loaded")

    app.logger.info("Loading config class from JSON")
    Config.load_config_from_json()
    app.logger.info("Config class loaded")

    from .routes import init_routes

    app.logger.info("Initializing routes")
    init_routes(app)
    app.logger.info("Routes initialized")

    app.logger.info("Flask app initialized")
    return app
