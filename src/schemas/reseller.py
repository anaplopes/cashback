from pydantic import BaseModel
from src.schemas.auth import Auth


class Reseller(BaseModel):
    name: str
    cpf: str
    auth: Auth
