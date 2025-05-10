from fastapi.responses import JSONResponse
import requests

from app.schema_validators import CreateRepoRequest
from app.utils import get_headers, error_handler

BASE_URL = "https://api.github.com"


class Repository:

    def __init__(self):
        self.session = requests.Session()

    def get_user_data(self, user_name: str):
        """Get user data."""
        try:
            url = f"{BASE_URL}/users/{user_name}"
            response = self.session.get(url, headers=get_headers())
            status_code = response.status_code
            if status_code != 200:
                return error_handler(status_code)
            return response.json(), status_code
        except Exception as e:
            content = {"error": str(e)}
            return JSONResponse(content=content, status_code=500)

    def list_repositories(self, user_name: str):
        """Get the list of repositories for a given user."""
        try:
            # TODO: start thinking about pagination
            url = f"{BASE_URL}/users/{user_name}/repos"
            response = self.session.get(url, headers=get_headers())
            status_code = response.status_code
            content = response.json()
            if status_code != 200:
                return error_handler(status_code)
            return JSONResponse(content=content, status_code=status_code)
        except Exception as e:
            content = {"error": str(e)}
            return JSONResponse(content=content, status_code=500)

    def create_repository(self, payload: CreateRepoRequest):
        """Create repository."""
        try:
            url = f"{BASE_URL}/user/repos"
            json = payload.model_dump(exclude_none=True)
            response = self.session.post(url, json=json, headers=get_headers())
            status_code = response.status_code
            if status_code != 201:
                return error_handler(status_code)
            return JSONResponse(content=response.json(), status_code=status_code)
        except Exception as e:
            content = {"error": str(e)}
            return JSONResponse(content=content, status_code=500)

    def delete_repository(self, owner: str, repo: str):
        """Delete repository."""
        try:
            url = f"{BASE_URL}/repos/{owner}/{repo}"
            response = self.session.delete(url, headers=get_headers())
            status_code = response.status_code
            if status_code != 204:
                return error_handler(status_code)
            return JSONResponse(content={}, status_code=status_code)
        except Exception as e:
            content = {"error": str(e)}
            return JSONResponse(content=content, status_code=500)

    def get_repository_data(self, owner: str, repo: str):
        """Get repository data."""
        try:
            url = f"{BASE_URL}/repos/{owner}/{repo}/pulls"
            response = self.session.get(url, headers=get_headers())
            status_code = response.status_code
            if status_code != 200:
                return error_handler(status_code)
            pull_requests_open = len(response.json())
            if pull_requests_open == 0:
                return error_handler(404)
            user_contributors_data = []
            for pr in response.json():
                user_name = pr["user"]["login"]
                user_data_response = self.get_user_data(user_name=user_name)
                email = user_data_response[0]["email"] if user_data_response[0]["email"] else "Email not found"
                user_contributors_data.append({"name": pr["user"]["login"], "email": email})
            content = user_contributors_data
            return JSONResponse(content=user_contributors_data, status_code=status_code)
        except Exception as e:
            content = {"error": str(e)}
            return JSONResponse(content=content, status_code=500)


repository = Repository()
