from fastapi import Response
from fastapi.responses import JSONResponse
import requests
import os

from app.schema_validators import CreateRepoRequest

TOKEN = os.getenv("GITHUB_TOKEN_CREDENTIAL")
BASE_URL = "https://api.github.com/"


class Repository:

    def list_repositories(self, user_name: str):
        """Get the list of repositories for a given user."""
        url = f"{BASE_URL}/users/{user_name}/repos"

        response = requests.get(url)

        if response.status_code != 200:
            return {"error": f"Unable to fetch {user_name} repositories"}, response.status_code
        repos = response.json()
        return repos, response.status_code

    def create_repository(self, payload: CreateRepoRequest):
        """Create repository."""
        url = f"{BASE_URL}/user/repos"
        headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
        json = payload.model_dump(exclude_none=True)
        response = requests.post(url, json=json, headers=headers)
        status_code = response.status_code
        if status_code != 201:
            return {"error": "Unable to create repository"}, status_code
        return JSONResponse(content=response.json(), status_code=status_code), status_code

    def delete_repository(self, owner: str, repo: str):
        """Delete repository."""
        url = f"{BASE_URL}/repos/{owner}/{repo}"
        headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
        response = requests.delete(url, headers=headers)
        status_code = response.status_code
        if status_code != 204:
            return {"error": "Unable to delete repository"}, status_code
        return Response(status_code=status_code), status_code


repository = Repository()
