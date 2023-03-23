from pydantic import BaseModel, EmailStr


class Auth(BaseModel):
    email: EmailStr
    password: str


class Reseller(Auth):
    name: str
    cpf: str
