"""
This module simply initializes all important things to build the webapplicatioln
"""

from flask import Flask
from src.routes import bp

def create_app(config_object='src.settings') -> Flask:

    app = Flask(__name__)
    app.config.from_object(config_object)
    init_extensions(app)
    app.register_blueprint(bp)

    return app

def init_extensions(app):
    from src.ext import db, migrate, bcrypt, jwt, ma
    # Import some of our extenisons

    db.init_app(app) # Databse
    db.app = app # this shouldn't be needed but it fails without it
    bcrypt.init_app(app) # Password hash generator
    migrate.init_app(app, db) # Database migrate tool (used for changing models)
    jwt.init_app(app) # webtoken module
    ma.init_app(app)
