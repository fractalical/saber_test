from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = [
    "BuildNotFound",
    "EmptyBuildName",
]


class BuildNotFound(BaseAPIException):
    message = "Build not fount."
    status_code = status.HTTP_404_NOT_FOUND


class EmptyBuildName(BaseAPIException):
    message = "Build name is required."
    status_code = status.HTTP_400_BAD_REQUEST
