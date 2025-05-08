from fastapi import Response
from fastapi.responses import JSONResponse
import requests

from app.schema_validators import CreateRepoRequest
from app.utils import get_headers

BASE_URL = "https://api.github.com/"


class Repository:

    def __init__(self):
        self.session = requests.Session()
        self.headers = get_headers()

    def get_user_data(self, user_name: str):
        """Get user data."""
        url = f"{BASE_URL}/users/{user_name}"
        response = self.session.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code != 200:
            return {"error": "Unable to fetch user data"}, status_code
        return response.json(), status_code

    def list_repositories(self, user_name: str):
        """Get the list of repositories for a given user."""
        url = f"{BASE_URL}/users/{user_name}/repos"
        response = self.session.get(url, headers=self.headers)

        if response.status_code != 200:
            return {"error": f"Unable to fetch {user_name} repositories"}, response.status_code
        repos = response.json()
        return repos, response.status_code

    def create_repository(self, payload: CreateRepoRequest):
        """Create repository."""
        url = f"{BASE_URL}/user/repos"
        json = payload.model_dump(exclude_none=True)
        response = self.session.post(url, json=json, headers=self.headers)
        status_code = response.status_code
        if status_code != 201:
            return {"error": "Unable to create repository"}, status_code
        return JSONResponse(content=response.json(), status_code=status_code), status_code

    def delete_repository(self, owner: str, repo: str):
        """Delete repository."""
        url = f"{BASE_URL}/repos/{owner}/{repo}"
        response = self.session.delete(url, headers=self.headers)
        status_code = response.status_code
        if status_code != 204:
            return {"error": "Unable to delete repository"}, status_code
        return Response(status_code=status_code), status_code

    def get_repository_data(self, owner: str, repo: str):
        """Get repository data."""
        url = f"{BASE_URL}/repos/{owner}/{repo}/pulls"
        response = self.session.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code != 200:
            return {"error": "Unable to fetch repository data"}, status_code
        pull_requests_open = len(response.json())
        if pull_requests_open == 0:
            return {"error": "No pull requests found"}, 404
        user_contributors_data = []
        for pr in response.json():
            user_name = pr["user"]["login"]
            user_data_response = self.get_user_data(user_name=user_name)
            email = user_data_response[0]["email"] if user_data_response[0]["email"] else "Email not found"
            user_contributors_data.append({"name": pr["user"]["login"], "email": email})
        return JSONResponse(content=user_contributors_data, status_code=status_code), status_code


repository = Repository()
