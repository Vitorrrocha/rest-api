import requests
import os

from app.schema_validators import CreateRepoRequest

TOKEN = os.getenv("GITHUB_TOKEN_CREDENTIAL")
BASE_URL = "https://api.github.com/"


class Repository:
    def list_repositories(self, username: str):
        """Get the list of repositories for a given user."""
        url = f"{BASE_URL}/users/{username}/repos"

        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Unable to fetch repositories"}, response.status_code
        repos = response.json()
        return repos, response.status_code

    def create_repository(self, payload: CreateRepoRequest):
        """Create repository."""
        url = f"{BASE_URL}/user/repos"
        headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
        json = payload.model_dump(exclude_none=True)
        response = requests.post(url, json=json, headers=headers)
        if response.status_code != 201:
            return {"error": "Unable to create repository"}, response.status_code
        return response.json(), response.status_code


repository = Repository()
