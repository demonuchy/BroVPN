from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import  ConfigDict
from pathlib import Path
from shared.logger.logger import logger

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
    DB_CONTAINER_NAME : str

    REDIS_HOST : str
    REDIS_PORT : str

    JWT_SECRET_KEY : str
    JWT_ACCESS_EXPIRE_MINETS : int
    JWT_REFRESH_EXPIRE_MINETS : int
    JWT_ALGORITM : str
    JWT_KID : str

    TOKEN_BOT : str
    WEBHOOK_TUNNEL_URL : str
    WEBHOOK_SECRET_KEY : str

    @property
    def AsyncDataBaseUrl(self):
        """Url для подключения к базе данных"""
        uri = None
        if self.DB_CONTAINER_NAME:
            uri = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_CONTAINER_NAME}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            uri = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        logger.debug(f"Uri подключения к дб {uri}")
        return uri

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        case_sensitive=False, 
        extra="ignore"
    )

config = Settings()