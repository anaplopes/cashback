from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    # API
    API_PREFIX: str = "/api/v1"
    API_VERSION: str = "0.1.0"

    # APP
    APP_NAME: str = "Cashback"
    APP_DESCRIPTION: str = "Sistema de cashback para compra de revendedoras."

    # API BOTICARIO
    GB_API_URL: str

    # DATABASE
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_URI: PostgresDsn
    DEBUG: bool

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
