""" Module starter"""
import os
from flask import Flask

from api.routes import init_routes


def create_app(test_config=None):
    """Creates the application"""
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "my_super_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    # initializing routes
    init_routes(app)

    return app
