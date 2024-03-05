import os

from pydantic import Field
from pydantic_settings import BaseSettings

from app.const import _ENV, LogLevel


class Settings(BaseSettings):
    ENV: _ENV = Field(
        _ENV.development,
        description="Environment",
    )
    LOG_LEVEL: LogLevel = Field(
        LogLevel.INFO,
        description="Logging level",
    )
    API_SECRET_KEY: str = Field(
        "secret",
        description="API secret key",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def _set_settings() -> Settings:
    _env = _ENV(os.getenv("ENV", "development"))
    _env_file = f".env.{_env.value}"
    Settings.Config.env_file = _env_file
    s = Settings()  # type: ignore
    return s


settings = _set_settings()
