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
    name = Field(description='Build name')
    tasks = Field(description='Tasks of build')


class BaseBuild(BaseModel):
    """Base model for build."""


class BuildName(BaseBuild):
    name: str = BuildFields.name


class BuildTasks(BaseBuild):
    tasks: List[str] = BuildFields.tasks


class Build(BaseBuild):
    name: str = BuildFields.name
    tasks: List[str] = BuildFields.tasks
