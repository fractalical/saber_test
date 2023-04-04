"""Module for load settings form `.env` or if server running with parameter
`dev` from `.env.dev`"""

from functools import lru_cache

from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.types import SecretStr

__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    class Config:
        """Configuration of settings."""

        #: str: env file encoding.
        env_file_encoding = "utf-8"
        #: str: allow custom fields in model.
        arbitrary_types_allowed = True


class Settings(_Settings):
    """Server settings.

    Formed from `.env` or `.env.dev`.
    """

    #: SecretStr: secret x-token for authority.
    X_API_TOKEN: SecretStr

    FILE_NAME: str

    LEVEL: int


@lru_cache()
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""
    return Settings(_env_file=find_dotenv(env_file))
