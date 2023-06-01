from flask import Flask, jsonify

from api.routes import init_routes


def create_app(test_config=None):
    # creates an application that is named after the name of the file
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "some_dev_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usr:pwd@pgsql:5432/todos"

    # initializing routes
    init_routes(app)

    return app
