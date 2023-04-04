from typing import List

from pydantic import Field

from app.pkg import models
from app.pkg.models.base import BaseModel

__all__ = [
    "BuildFields",
    "BaseBuild",
    "BuildName",
    "BuildTasks",
    "Build",
]


class BuildFields:
    build = Field(description='Build name')
    tasks = Field(description='Tasks of build')


class BaseBuild(BaseModel):
    """Base model for build."""


class BuildName(BaseBuild):
    build: str = BuildFields.build


class BuildTasks(BaseBuild):
    tasks: List[str] = BuildFields.tasks


class Build(BaseBuild):
    build: str = BuildFields.build
    tasks: List[str] = BuildFields.tasks
