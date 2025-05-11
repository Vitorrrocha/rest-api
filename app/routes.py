from fastapi import APIRouter

from app.use_cases.repository import repository
from app.schema_validators import CreateRepoRequest

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/user/{user_name}/repos")
def on_user_list_repos(user_name: str):
    """List all user repositories."""
    response = repository.list_repositories(user_name)
    return response


@router.post("/create/repo")
def on_create_user_repo(payload: CreateRepoRequest):
    """Create a repository."""
    response = repository.create_repository(payload)
    return response


@router.delete("/delete/{owner}/{repo}")
def on_delete_user_repo(owner: str, repo: str):
    """Delete a repository."""
    response = repository.delete_repository(owner=owner, repo=repo)
    return response


@router.get("/repo/data/{owner}/{repo}")
def on_get_repo_data(owner: str, repo: str):
    """Get repository data."""
    response = repository.get_repository_data(owner=owner, repo=repo)
    return response
