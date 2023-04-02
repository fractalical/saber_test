from typing import List

from pydantic import Field

from app.pkg.models.base import BaseModel

__all__ = [
    "TaskFields",
    "BaseTask",
    "TaskName",
    "TaskDependencies",
    "Task",
]


class TaskFields:
    name = Field(description='Task name')
    dependencies = Field(description='Dependencies of task')


class BaseTask(BaseModel):
    """Base model for task."""


class TaskName(BaseTask):
    name: str = TaskFields.name


class TaskDependencies(BaseTask):
    dependencies: List[str] = TaskFields.dependencies


class Task(BaseTask):
    name: str = TaskFields.name
    dependencies: List[str] = TaskFields.dependencies
