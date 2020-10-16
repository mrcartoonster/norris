# -*- coding: utf-8 -*-
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base Config with default."""

    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="YO_MAMA")
    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Development Config This is the dev config."""

    DEBUG = True


class TestingConfig(Config):
    """Testing config to run tests."""

    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    FLASK_ENV = "production"
