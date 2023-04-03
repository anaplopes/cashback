import os
import logging
from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    # API
    API_PREFIX: str = "/api/v1"
    API_VERSION: str = "0.1.0"

    # APP
    ENVIRONMENT: str = "dev"
    DEBUG: bool = False
    APP_NAME: str = "Cashback"
    APP_DESCRIPTION: str = "Sistema de cashback para compra de revendedoras."

    # DATABASE
    DB_URI: PostgresDsn

    # API BOTICARIO
    GB_API_URL: str
    GB_TOKEN: str

    class Config:
        case_sensitive = True


log = logging.getLogger("uvicorn")
log.info("Loading config settings from the environment...")


environment = os.getenv("ENVIRONMENT", "dev")
settings = Settings(_env_file=f".env.{environment}")
