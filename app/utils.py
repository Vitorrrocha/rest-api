import os

TOKEN = os.getenv("GITHUB_TOKEN_CREDENTIAL")


def get_headers():
    """Get header."""
    return {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
