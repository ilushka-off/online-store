import functools
import os
import pathlib

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="core/.env")

    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
    ENVIRONMENT: str = "local"

    CORS_ALLOW_ORIGIN_LIST: str = "http://localhost:8000"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    SESSION_MIDDLEWARE_SECRET: str = "online-store"

    @property
    def cors_allow_origins(self) -> list[str]:
        return self.CORS_ALLOW_ORIGIN_LIST.split("&")

    @property
    def postgres_dsn(self) -> str:
        database = (
            self.POSTGRES_DB
            if self.ENVIRONMENT != "test"
            else f"{self.POSTGRES_DB}_test"
        )
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{database}"
        )


@functools.lru_cache
def settings() -> Settings:
    return Settings()


logger.add(
    os.path.join(settings().BASE_DIR.parent, "logs/errors/log_{time}.log"),
    level="ERROR",
    format="{time} {message}",
    rotation="1 day",
)
logger.add(
    os.path.join(settings().BASE_DIR.parent, "logs/info/log_{time}.log"),
    level="INFO",
    format="{time} {level} {message}",
    rotation="1 day",
)
