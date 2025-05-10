import os
from fastapi.responses import JSONResponse

TOKEN = os.getenv("GITHUB_TOKEN_CREDENTIAL")


def get_headers():
    """Get header."""
    return {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}


def error_handler(status_code: int):
    """Check status code."""
    if status_code == 304:
        content = {"error": "Not modified"}
        return JSONResponse(content=content, status_code=status_code)
    elif status_code == 400:
        content = {"error": "Bad Request"}
        return JSONResponse(content=content, status_code=status_code)
    elif status_code == 401:
        content = {"error": "Requires authentication"}
        return JSONResponse(content=content, status_code=status_code)
    elif status_code == 403:
        content = {"error": "Forbidden"}
        return JSONResponse(content=content, status_code=status_code)
    elif status_code == 404:
        content = {"error": "Resource not found"}
        return JSONResponse(content=content, status_code=status_code)
    elif status_code == 422:
        content = {"error": "Validation failed or endpoint has been spammed"}
        return JSONResponse(content=content, status_code=status_code)
