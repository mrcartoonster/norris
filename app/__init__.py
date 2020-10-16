# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf_protection = CSRFProtect()


def create_app():
    """Main Flask app."""
    app = Flask(__name__)

    config_type = os.getenv("CONFIG_TYPE", "config.DevelopmentConfig")
    app.config.from_object(config_type)


def register_blueprints(app):
    """Blueprints and routes used in this Flask app."""
    pass


def initialize_extensions(app):
    """Third Party Modules.

    Below are third party modules this Flask app uses.

    """
    csrf_protection.init_app(app)
