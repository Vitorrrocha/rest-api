from fastapi import APIRouter, HTTPException
from typing import Union
from app.use_cases.repository import repository

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/user/{user_name}/repos")
def on_user_repos(user_name: str):
    response, status_code = repository.list_repository(user_name)
    if status_code == 200:
        return response
    else:
        raise HTTPException(status_code=status_code, detail=response)
