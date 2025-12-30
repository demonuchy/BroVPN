from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import  ConfigDict
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent  # shared/ -> backend/
ENV_PATH = BASE_DIR/".env"
print(ENV_PATH)


class Settings(BaseSettings):
    """Настройкт проекта"""

    DB_USER : str 
    DB_PASS : str 
    DB_HOST : str 
    DB_NAME : str
    DB_PORT : int 

    REDIS_HOST : str
    REDIS_PORT : str

    JWT_SECRET_KEY : str
    JWT_ACCESS_EXPIRE_MINETS : int
    JWT_REFRESH_EXPIRE_MINETS : int
    JWT_ALGORITM : str
    JWT_KID : str

    @property
    def AsyncDataBaseUrl(self):
        """Url для подключения к базе данных"""
        uri = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return uri

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        case_sensitive=False, 
        extra="ignore"
    )

config = Settings()