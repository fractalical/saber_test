from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = [
    "CircularDependency",
    "NotFoundTask",
]


class CircularDependency(BaseAPIException):
    message = "Circular dependency detected."
    status_code = status.HTTP_508_LOOP_DETECTED


class NotFoundTask(BaseAPIException):
    message = "Some task not found."
    status_code = status.HTTP_404_NOT_FOUND
