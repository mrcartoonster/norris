# -*- coding: utf-8 -*-
import pytest

from app import create_app


@pytest.fixture(scope="module")
def test_client():
    """Fixture for functional test to get app context."""
    flask_app = create_app()
    flask_app.config.from_object("config.TestingConfig")

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
