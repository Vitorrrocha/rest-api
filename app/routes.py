from fastapi import APIRouter, HTTPException
from typing import Union

from app.use_cases.repository import repository
from app.schema_validators import CreateRepoRequest

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/user/{user_name}/repos")
def on_user_list_repos(user_name: str):
    response, status_code = repository.list_repositories(user_name)
    if status_code == 200:
        return response
    else:
        raise HTTPException(status_code=status_code, detail=response)


@router.post("/create/repo")
def on_create_user_repo(payload: CreateRepoRequest):
    response, status_code = repository.create_repository(payload)
    if status_code == 201:
        return response
    else:
        raise HTTPException(status_code=status_code, detail=response)


@router.delete("/delete/{owner}/{repo}")
def on_delete_user_repo(owner: str, repo: str):
    """Delete a repository."""
    response, status_code = repository.delete_repository(owner=owner, repo=repo)
    if status_code == 204:
        return response
    else:
        raise HTTPException(status_code=status_code, detail=response)
