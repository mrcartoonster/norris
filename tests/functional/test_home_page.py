# -*- coding: utf-8 -*-
"""Tests that will make sure everything apperson on the home page correctly."""


def test_home_get(test_client):
    """
    1. GIVEN Flask application
    2. WHEN a (GET) request to '/'
    3. THEN a homepage will display correct test.
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Norriss Jokes" in response.data
    assert b"About" in response.data
    assert b"Get Another Joke" in response.data


def test_home_post(test_client, success_chuck):
    """
    1. GIVEN a Flask application
    2. WHEN a (POST) request is given
    3. THEN a Chuck Norriss jock is returned and shown.
    """
    response = test_client.post("/")
    assert response.status_code == 200
    assert b"About" in response.data
    assert b"Chuck Norris CAN kill you in your dreams" in response.data
