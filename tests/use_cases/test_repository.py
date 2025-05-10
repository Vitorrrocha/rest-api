from unittest.mock import patch, MagicMock
import pytest
from app.use_cases.repository import repository, BASE_URL


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.get")
def test_list_repository_happy_case(mock_session_get, mock_headers, mock_error_handler):
    """Test list repository happy case."""
    mock_session_get.return_value = MagicMock()
    mock_session_get.return_value.status_code = 200
    mock_session_get.return_value.json.return_value = {"value": "ok"}
    mock_headers.return_value = {"happy": "case"}
    user_name = "test_user"
    response = repository.list_repositories(user_name)
    mock_session_get.assert_called_once_with(f"{BASE_URL}/users/{user_name}/repos", headers={"happy": "case"})
    assert response.status_code == 200
    assert response.body == b'{"value":"ok"}'
    mock_error_handler.assert_not_called()


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.get")
def test_list_repository_error_case(mock_session_get, mock_headers, mock_error_handler):
    """Test list repository happy case."""
    mock_session_get.return_value = MagicMock()
    mock_session_get.return_value.status_code = 400
    mock_headers.return_value = {"error": "case"}
    user_name = "test_user"
    response = repository.list_repositories(user_name)
    mock_session_get.assert_called_once_with(f"{BASE_URL}/users/{user_name}/repos", headers={"error": "case"})
    mock_error_handler.assert_called_once_with(400)


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.post")
def test_create_repository_happy_case(mock_session_post, mock_headers, mock_error_handler):
    """Test create repository happy case."""
    mock_session_post.return_value = MagicMock()
    mock_session_post.return_value.status_code = 201
    mock_session_post.return_value.json.return_value = {"value": "ok"}
    mock_headers.return_value = {"happy": "case"}
    payload = MagicMock()
    payload.model_dump.return_value = {"payload": "ok"}
    response = repository.create_repository(payload)
    mock_session_post.assert_called_once_with(f"{BASE_URL}/user/repos", json={"payload": "ok"}, headers={"happy": "case"})
    assert response.status_code == 201
    assert response.body == b'{"value":"ok"}'
    mock_error_handler.assert_not_called()


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.post")
def test_create_repository_error_case(mock_session_post, mock_headers, mock_error_handler):
    """Test create repository error case."""
    mock_session_post.return_value = MagicMock()
    mock_session_post.return_value.status_code = 400
    mock_session_post.return_value.json.return_value = {"error": "ok"}
    mock_headers.return_value = {"error": "case"}
    payload = MagicMock()
    payload.model_dump.return_value = {"payload": "ok"}
    response = repository.create_repository(payload)
    mock_session_post.assert_called_once_with(f"{BASE_URL}/user/repos", json={"payload": "ok"}, headers={"error": "case"})
    mock_error_handler.assert_called_once_with(400)


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.delete")
def test_delete_repository_happy_case(mock_session_delete, mock_headers, mock_error_handler):
    """Test delete repository happy case."""
    mock_session_delete.return_value = MagicMock()
    mock_session_delete.return_value.status_code = 204
    mock_headers.return_value = {"happy": "case"}
    owner = "test_owner"
    repo = "test_repo"
    response = repository.delete_repository(owner=owner, repo=repo)
    mock_session_delete.assert_called_once_with(f"{BASE_URL}/repos/{owner}/{repo}", headers={"happy": "case"})
    assert response.status_code == 204
    assert response.body == b"{}"
    mock_error_handler.assert_not_called()


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.delete")
def test_delete_repository_error_case(mock_session_delete, mock_headers, mock_error_handler):
    """Test delete repository error case."""
    mock_session_delete.return_value = MagicMock()
    mock_session_delete.return_value.status_code = 400
    mock_headers.return_value = {"error": "case"}
    owner = "test_owner"
    repo = "test_repo"
    response = repository.delete_repository(owner=owner, repo=repo)
    mock_session_delete.assert_called_once_with(f"{BASE_URL}/repos/{owner}/{repo}", headers={"error": "case"})
    mock_error_handler.assert_called_once_with(400)


@patch("app.use_cases.repository.json")
@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.get_user_data")
@patch("app.use_cases.repository.repository.session.get")
def test_get_repository_data_happy_case(mock_session_get, mock_get_user_data, headers, mock_error_handler, mock_json):
    """Test get repository data happy case."""
    mock_session_get.return_value = MagicMock()
    mock_session_get.return_value.status_code = 200
    mock_user = [{"user": {"login": "test_user"}}]
    mock_session_get.return_value.json.return_value = mock_user
    headers.return_value = {"happy": "case"}
    mock_get_user_data.return_value = MagicMock()
    mock_get_user_data.return_value.status_code = 200
    mock_json.loads.return_value = {"email": "test_email"}
    owner = "test_owner"
    repo = "test_repo"
    response = repository.get_repository_data(owner=owner, repo=repo)
    mock_session_get.assert_called_once_with(f"{BASE_URL}/repos/{owner}/{repo}/pulls", headers={"happy": "case"})
    mock_get_user_data.assert_called_once_with(user_name="test_user")
    assert response.status_code == 200
    assert response.body == b'[{"name":"test_user","email":"test_email"}]'
    mock_error_handler.assert_not_called()


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.get_user_data")
@patch("app.use_cases.repository.repository.session.get")
def test_get_repository_data_error_case(mock_session_get, mock_get_user_data, mock_headers, mock_error_handler):
    """Test get repository data error case."""
    mock_session_get.return_value = MagicMock()
    mock_session_get.return_value.status_code = 400
    mock_headers.return_value = {"error": "case"}
    owner = "test_owner"
    repo = "test_repo"
    response = repository.get_repository_data(owner=owner, repo=repo)
    mock_session_get.assert_called_once_with(f"{BASE_URL}/repos/{owner}/{repo}/pulls", headers={"error": "case"})
    mock_error_handler.assert_called_once_with(400)
    mock_get_user_data.assert_not_called()


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.get")
def test_get_user_data_happy_case(mock_session_get, mock_headers, mock_error_handler):
    """Test get user data happy case."""
    mock_session_get.return_value = MagicMock()
    mock_session_get.return_value.status_code = 200
    mock_session_get.return_value.json.return_value = {"value": "ok"}
    mock_headers.return_value = {"happy": "case"}
    user_name = "test_user"
    response = repository.get_user_data(user_name)
    mock_session_get.assert_called_once_with(f"{BASE_URL}/users/{user_name}", headers={"happy": "case"})
    assert response.status_code == 200
    assert response.body == b'{"value":"ok"}'
    mock_error_handler.assert_not_called()


@patch("app.use_cases.repository.error_handler")
@patch("app.use_cases.repository.get_headers")
@patch("app.use_cases.repository.repository.session.get")
def test_get_user_data_error_case(mock_session_get, mock_headers, mock_error_handler):
    """Test get user data error case."""
    mock_session_get.return_value = MagicMock()
    mock_session_get.return_value.status_code = 400
    mock_headers.return_value = {"error": "case"}
    user_name = "test_user"
    response = repository.get_user_data(user_name)
    mock_session_get.assert_called_once_with(f"{BASE_URL}/users/{user_name}", headers={"error": "case"})
    mock_error_handler.assert_called_once_with(400)
