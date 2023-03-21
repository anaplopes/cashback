from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API: str = "/api"
    RPC: str = "/rpc"
    DOCS: str = "/docs"
    NAME: str = "Cashback"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Sistema de cashback para compra de revendedoras."

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URI: PostgresDsn | None = None


settings = Settings()
