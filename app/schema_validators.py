from pydantic import BaseModel, Field
from typing import Optional, Literal


class CreateRepoRequest(BaseModel):
    name: str
    description: Optional[str] = None
    homepage: Optional[str] = None
    private: Optional[bool] = Field(default=False)
    has_issues: Optional[bool] = Field(default=True)
    has_projects: Optional[bool] = Field(default=True)
    has_wiki: Optional[bool] = Field(default=True)
    has_discussions: Optional[bool] = Field(default=False)
    team_id: Optional[int] = None
    auto_init: Optional[bool] = Field(default=False)
    gitignore_template: Optional[str] = None
    license_template: Optional[str] = None
    allow_squash_merge: Optional[bool] = Field(default=True)
    allow_merge_commit: Optional[bool] = Field(default=True)
    allow_rebase_merge: Optional[bool] = Field(default=True)
    allow_auto_merge: Optional[bool] = Field(default=False)
    delete_branch_on_merge: Optional[bool] = Field(default=False)

    squash_merge_commit_title: Optional[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]] = None
    squash_merge_commit_message: Optional[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]] = None
    merge_commit_title: Optional[Literal["PR_TITLE", "MERGE_MESSAGE"]] = None
    merge_commit_message: Optional[Literal["PR_TITLE", "PR_BODY", "BLANK"]] = None

    has_downloads: Optional[bool] = Field(default=True)
    is_template: Optional[bool] = Field(default=False)
