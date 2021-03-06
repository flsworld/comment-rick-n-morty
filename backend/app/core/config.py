from databases import DatabaseURL
from pydantic import BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    config = Config(".env")
    PROJECT_NAME = "Commentez Rick & Morty"
    VERSION = "1.0.0"
    API_PREFIX = "/api"

    POSTGRES_USER = config("POSTGRES_USER", cast=str)
    # POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
    POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="postgres")
    POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
    POSTGRES_DB = config("POSTGRES_DB", cast=str)

    DATABASE_URL = config(
        "DATABASE_URL",
        cast=DatabaseURL,
        default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",  # noqa: E501
    )

    FIRST_SUPERUSER = "friedrich@frederic.fred"
    FIXTURES_PATH = "/backend/app/db/fixtures"

    class Config:
        env_file = "./env"


settings = Settings()
