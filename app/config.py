from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str
    model_config = SettingsConfigDict(env_file=".env")


# Singleton pattern to ensure only one settings instance
@lru_cache()
def get_settings() -> "Settings":
    return Settings()
