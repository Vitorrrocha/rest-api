import requests

base_url = "https://api.github.com/"


class Repository:
    def list_repository(self, username: str):
        """
        Get the list of repositories for a given user.
        """
        url = f"{base_url}/users/{username}/repos"

        response = requests.get(url)

        if response.status_code == 200:
            repos = response.json()
            return repos, response.status_code
        else:
            return {"error": "Unable to fetch repositories"}, response.status_code


repository = Repository()
