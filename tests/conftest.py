# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Dict

import pytest
import requests

from app import create_app

###############################################################################
# The Chuck Norris app has three API calls Listing each call below:
# 1. https://api.chucknorris.io/jokes/random This will be our first mock
# 2. https://api.chucknorris.io/jokes/random?category={category}
#   You'll place the category of joke you want here. You can use this to test
#   for HTTP 400 later on when you add this API call.
# 3. https://api.chucknorris.io/jokes/categories
#   This list the categories. We'll mock this because our site will have a drop
#   down for this later on. We'll make a mock for it
# 4. https://api.chucknorris.io/jokes/search?query={query} You can use this to
# search for maybe specific joke:
# e.g https://api.chucknorris.io/jokes/search?query=fist this query outputs 50
# jokes for you. Its a list of results with jokes that have fists in them. Pun
# intended since it's about Chuck Norriss;)
#
#
###############################################################################

# Below are the Mocks


def response_headers():
    """For dataclass default factory."""
    return {
        "Date": "Sat, 17 Oct 2020 05:02:03 GMT",
        "Content-Type": "application/json;charset=UTF-8",
        "Transfer-Encoding": "chunked",
        "Connection": "keep-alive",
        "Set-Cookie": (
            "__cfduid=dd60d9b05e0954f429392832eb9321a361602910922; "
            "expires=Mon, 16-Nov-20 05:02:02 GMT; path=/; domain="
            ".chucknorris.io; HttpOnly; SameSite=Lax"
        ),
        "Via": "1.1 vegur",
        "CF-Cache-Status": "DYNAMIC",
        "cf-request-id": "05d688bf98000027dcf19b0000000001",
        "Expect-CT": (
            "max-age=604800, report-uri="
            '"https://report-uri.cloudflare'
            '.com/cdn-cgi/beacon/expect-ct"'
        ),
        "Report-To": (
            '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.'
            'com\\/report?lkg-colo=143&lkg-time=1602910923"}]'
            ',"group":"cf-nel","max_age":604800}'
        ),
        "NEL": '{"report_to":"cf-nel","max_age":604800}',
        "Server": "cloudflare",
        "CF-RAY": "5e3777128fac27dc-SLC",
        "Content-Encoding": "gzip",
    }


@dataclass
class MockChuckSuccess:
    status_code: int = 200
    headers: Dict[str, str] = field(default_factory=response_headers)
    url: str = ""

    def json(self):
        return {
            "categories": [],
            "created_at": "2020-01-05 13:42:24.696555",
            "icon_url": (
                "https://assets.chucknorris.host/img/avatar/chuck-norris.png"
            ),
            "id": "7upzDPIQS6ChFwLOHEnvFA",
            "updated_at": "2020-01-05 13:42:24.696555",
            "url": "https://api.chucknorris.io/jokes/7upzDPIQS6ChFwLOHEnvFA",
            "value": "Chuck Norris CAN kill you in your dreams.",
        }


@pytest.fixture(scope="module")
def test_client():
    """Fixture for functional test to get app context."""
    flask_app = create_app()
    flask_app.config.from_object("config.TestingConfig")

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope="function")
def success_chuck(monkeypatch):
    """This is a fixture making a successful mock request to the Chuck Norriss
    API.

    It's using the MockChuckSuccess mock class.

    """

    def get_mock(url):
        return MockChuckSuccess(url)

    # url = "https://api.chucknorris.io/jokes/random"

    monkeypatch.setattr(requests, "get", get_mock)
