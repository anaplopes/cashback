from datetime import datetime, date
from pydantic import BaseModel, UUID4


class Purchase(BaseModel):
    code: str
    date: date
    value: float
    cpf: str


class PurchaseSchema(Purchase):
    id: UUID4
    status: str
    created_at: datetime
    val_cashback: float
    per_cashback: float
