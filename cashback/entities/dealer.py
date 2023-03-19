from pydantic import BaseModel
from cashback.entities.auth import Auth


class Dealer(BaseModel):
    name: str
    cpf: str
    auth: Auth
