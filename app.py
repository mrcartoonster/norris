# -*- coding: utf-8 -*-
"""For deployment with gunicorn instance to catch."""
from app import create_app

app = create_app()
