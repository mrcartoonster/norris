# -*- coding: utf-8 -*-
"""Flask app factory.

Following Pat Kennedy's template.

"""
import os

import requests
import requests_cache
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

from .forms import Joke

csrf_protection = CSRFProtect()


def create_app():
    """Main Flask app."""
    app = Flask(__name__)

    config_type = os.getenv("CONFIG_TYPE", "config.DevelopmentConfig")
    app.config.from_object(config_type)

    initialize_extensions(app)

    requests_cache.install_cache(
        "simple_cache",
        backend="sqlite",
        expire_after=5,
    )

    @app.route("/", methods=["GET", "POST"])
    def index():
        """Home page with joke."""
        form = Joke()
        r = None
        if form.validate_on_submit():
            url = "https://api.chucknorris.io/jokes/random"
            r = requests.get(url).json()
        return render_template("base.html", form=form, r=r)

    @app.route("/about")
    def about():
        """The about page."""
        pass

    return app


def initialize_extensions(app):
    """Third Pary Modules.

    Below are third party modules used in this Flask App.

    """
    csrf_protection.init_app(app)
