# -*- coding: utf-8 -*-
"""Flask forms for home page."""
from flask_wtf import FlaskForm
from wtforms import SubmitField


class Joke(FlaskForm):
    """The get a new jock submit button.

    For right now only need a button. Might remove since we don't need
    tokens. Holding due to we may be adding searching.

    """

    submit = SubmitField("Get Another Joke")
