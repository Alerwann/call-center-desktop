# # app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    MONGODB_URI: str  # obligatoire, erreur si manquant

    # JWT secrets (obligatoires)
    JWT_SECRET: str
    JWT_EXPIRES_IN: str = "15m"
    REFRESH_TOKEN_SECRET: str
    REFRESH_TOKEN_EXPIRE_IN: str = "7d"

    # Server
    port: int = 8000
    cors_origins: list[str] = ["http://localhost:3000"]

    # Environment
    ENVIRONEMENT: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )


# Instance globale
settings = Settings() # type: ignore
