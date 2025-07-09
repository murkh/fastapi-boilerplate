import os
from enum import Enum


from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "Tattvan Eclinic")
    APP_DESCRIPTION: str = os.getenv("APP_DESCRIPTION", "Tattvan Eclinic API")
    APP_VERSION: str | None = os.getenv("APP_VERSION", None)


class CryptSettings(BaseSettings):
    SECRET_KEY: SecretStr = os.getenv("SECRET_KEY", "testing")
    ALGORITHM: str = os.getenv("ALGORITHM", default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES", default=30
    )
    REFRESH_TOKEN_EXPIRE_DAYS: int = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", default=7)


class DatabaseSettings(BaseSettings):
    pass


class PostgresSettings(DatabaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", default="postgres")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", default=5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", default="tattvan")
    POSTGRES_SYNC_PREFIX: str = os.getenv(
        "POSTGRES_SYNC_PREFIX", default="postgresql://"
    )
    POSTGRES_ASYNC_PREFIX: str = os.getenv(
        "POSTGRES_ASYNC_PREFIX", default="postgresql+asyncpg://"
    )
    POSTGRES_URI: str = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    POSTGRES_URL: str | None = os.getenv("POSTGRES_URL", default=None)


class ClientSideCacheSettings(BaseSettings):
    CLIENT_CACHE_MAX_AGE: int = os.getenv("CLIENT_CACHE_MAX_AGE", default=60)


class EnvironmentOption(Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = os.getenv(
        "ENVIRONMENT", default=EnvironmentOption.LOCAL
    )


class Settings(
    AppSettings,
    PostgresSettings,
    CryptSettings,
    ClientSideCacheSettings,
    EnvironmentSettings,
):
    pass


settings = Settings()
