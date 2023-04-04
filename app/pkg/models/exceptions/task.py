from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = [
    "CircularDependency",
]


class CircularDependency(BaseAPIException):
    message = "Circular dependency detected."
    status_code = status.HTTP_508_LOOP_DETECTED
