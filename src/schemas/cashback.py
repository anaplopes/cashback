from pydantic import BaseModel


class Body(BaseModel):
    credit: int


class Cashback(BaseModel):
    statusCode: int
    body: Body
