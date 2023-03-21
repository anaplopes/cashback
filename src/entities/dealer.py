from pydantic import BaseModel
from src.entities.auth import Auth


class Dealer(BaseModel):
    name: str
    cpf: str
    auth: Auth
