from unittest.mock import patch
from app.utils import get_headers, error_handler


@patch("app.utils.TOKEN", "test_token")
def test_get_headers():
    """Test get headers."""
    headers = get_headers()
    assert headers == {"Authorization": "Bearer test_token", "Accept": "application/vnd.github+json"}


def test_error_handler_should_return_304():
    """Test check status code."""
    status_code = 304
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Not modified"}'


def test_error_handler_should_return_400():
    """Test check status code."""
    status_code = 400
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Bad Request"}'


def test_error_handler_should_return_401():
    """Test check status code."""
    status_code = 401
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Requires authentication"}'


def test_error_handler_should_return_403():
    """Test check status code."""
    status_code = 403
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Forbidden"}'


def test_error_handler_should_return_404():
    """Test check status code."""
    status_code = 404
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Resource not found"}'


def test_error_handler_should_return_422():
    """Test check status code."""
    status_code = 422
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Validation failed or endpoint has been spammed"}'


def test_error_handler_should_return_500():
    """Test check status code."""
    status_code = 500
    response = error_handler(status_code)
    assert response.status_code == status_code
    assert response.body == b'{"error":"Internal server error"}'
