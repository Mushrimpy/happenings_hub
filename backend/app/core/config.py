import secrets
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_URI: str = os.environ.get("DB_URI")
    DB_NAME: str = os.environ.get("DB_NAME")
    API_V1_STR: str = os.environ.get("API_V1_STR")
    FRONTEND_HOST: str = os.environ.get("FRONTEND_HOST")
    BACKEND_CORS_ORIGINS: str = os.environ.get("BACKEND_CORS_ORIGINS")
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"


settings = Settings()
