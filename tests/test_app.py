"""
This module contains tests for the FastAPI application defined in `app.py`. It
uses the `TestClient` from FastAPI to simulate HTTP requests to the application
and verify its behavior. The tests ensure that the application responds
correctly to various endpoints and scenarios.
"""

from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_todo.app import app


def test_read_root():
    """
    this test has 3 times (AAA)
    - Arrange: Set up the test client and any necessary preconditions.
    - Act: Send a GET request to the root endpoint ('/') of the FastAPI
    application.
    - Assert: Verify that the response status code is 200 (OK) and that the
    response JSON contains the expected greeting message.

    This test sends a GET request to the root endpoint ('/') and verifies that
    the response status code is 200 (OK) and that the response JSON contains
    the expected greeting message.
    """
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
