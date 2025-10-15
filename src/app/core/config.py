import os
from dotenv import load_dotenv
from enum import Enum
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings


current_file_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.abspath(os.path.join(current_file_dir, "..", "..", "..", ".env"))
load_dotenv(env_path)


class EnvironmentOption(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class AppSettings(BaseSettings):
    APP_NAME: str = Field(default="Falcon Backend")
    APP_DESCRIPTION: str = Field(default="Falcon Backend API")
    APP_VERSION: str | None = Field(default=None)


class CryptSettings(BaseSettings):
    SECRET_KEY: SecretStr = Field(default=SecretStr("testing"))
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7)


class DatabaseSettings(BaseSettings):
    pass


class PostgresqlSettings(DatabaseSettings):
    POSTGRES_USER: str = Field(default="postgres")
    POSTGRES_PASSWORD: str = Field(default="postgres")
    POSTGRES_SERVER: str = Field(default="localhost")
    POSTGRES_PORT: int = Field(default=5432)
    POSTGRES_DB: str
    POSTGRES_SYNC_PREFIX: str = Field(default="postgresql://")
    POSTGRES_ASYNC_PREFIX: str = Field(default="postgresql+asyncpg://")

    @property
    def POSTGRES_URI(self) -> str:
        return f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


class ClientSideSettings(BaseSettings):
    CLIENT_CACHE_MAX_AGE: int = Field(default=60)


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = Field(default=EnvironmentOption.LOCAL)


class Settings(
    AppSettings,
    CryptSettings,
    PostgresqlSettings,
    EnvironmentSettings,
):
    class Config:
        fields = {
            "APP_NAME": {"env": "APP_NAME"},
            "APP_DESCRIPTION": {"env": "APP_DESCRIPTION"},
            "APP_VERSION": {"env": "APP_VERSION"},
            "SECRET_KEY": {"env": "SECRET_KEY"},
            "ALGORITHM": {"env": "ALGORITHM"},
            "ACCESS_TOKEN_EXPIRE_MINUTES": {"env": "ACCESS_TOKEN_EXPIRE_MINUTES"},
            "REFRESH_TOKEN_EXPIRE_DAYS": {"env": "REFRESH_TOKEN_EXPIRE_DAYS"},
            "POSTGRES_USER": {"env": "POSTGRES_USER"},
            "POSTGRES_PASSWORD": {"env": "POSTGRES_PASSWORD"},
            "POSTGRES_SERVER": {"env": "POSTGRES_SERVER"},
            "POSTGRES_PORT": {"env": "POSTGRES_PORT"},
            "POSTGRES_DB": {"env": "POSTGRES_DB"},
            "POSTGRES_SYNC_PREFIX": {"env": "POSTGRES_SYNC_PREFIX"},
            "POSTGRES_ASYNC_PREFIX": {"env": "POSTGRES_ASYNC_PREFIX"},
            "POSTGRES_URL": {"env": "POSTGRES_URL"},
            "CLIENT_CACHE_MAX_AGE": {"env": "CLIENT_CACHE_MAX_AGE"},
            "ENVIRONMENT": {"env": "ENVIRONMENT"},
        }


settings = Settings()
