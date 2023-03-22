from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PREFIX_API: str = "/api/v1"
    NAME: str = "Cashback"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Sistema de cashback para compra de revendedoras."

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_URL: PostgresDsn
    DEBUG: bool

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
