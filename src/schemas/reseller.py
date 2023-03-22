from pydantic import BaseModel, EmailStr


class Reseller(BaseModel):
    name: str
    cpf: str
    email: EmailStr
    password: str


class Auth(BaseModel):
    email: EmailStr
    password: str
