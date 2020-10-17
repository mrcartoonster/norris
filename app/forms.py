# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField


class Joke(FlaskForm):
    """The get a new jock submit button."""

    submit = SubmitField("Get Another Joke")
