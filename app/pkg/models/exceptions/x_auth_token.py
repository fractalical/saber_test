from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = [
    "InvalidCredentials",
    "Unauthorized",
    "NoRights"
]


class InvalidCredentials(BaseAPIException):
    message = "Could not validate credentials."
    status_code = status.HTTP_403_FORBIDDEN


class Unauthorized(BaseAPIException):
    message = "User is not authorized"
    status_code = status.HTTP_401_UNAUTHORIZED


class NoRights(BaseAPIException):
    message = "User have not enough rights"
    status_code = status.HTTP_403_FORBIDDEN
