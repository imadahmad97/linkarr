from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)

    print("Loading config...")
    app.config.from_object(Config)  # Load config

    print(
        f"App config loaded with target_dir: {app.config.get('target_dir')}"
    )  # Debugging print

    from .routes import init_routes

    init_routes(app)

    return app
