from unittest.mock import patch, MagicMock
import pytest

from app.utils import get_headers


@patch("app.utils.TOKEN", "test_token")
def test_get_headers():
    """Test get headers."""
    headers = get_headers()
    assert headers == {"Authorization": "Bearer test_token", "Accept": "application/vnd.github+json"}
