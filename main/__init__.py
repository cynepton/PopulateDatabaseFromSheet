"""Main Application Factory

This is where the main application function is setup. It exposes a function \
that can be called by the entry app file.\n
The Flask Application factory method is used.
""" 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import config_by_name

db = SQLAlchemy()
cors = CORS()

def createApp(config_name="development"):
    """
    This function contains the application setup and configuration details. \n
    It takes the configuration environment and returns the Flask App.\n

    The allowed configuration options are `development`, `testing` and `production`.
    """
    app = Flask(__name__)

    # Import configuration based on config_name function parameter
    app.config.from_object(config_by_name[config_name])

    # Bind app to SQLAlchemy instance
    db.init_app(app)

    # Initialize CORS
    cors.init_app(app)

    return app
