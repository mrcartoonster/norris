# -*- coding: utf-8 -*-
"""The Norriss blueprint will be handling the API call returns.

This blueprint will output the joke to be shown

"""
from flask import Blueprint

norriss = Blueprint("norriss", __name__, template_folder="templates")

from . import routes
