from datetime import date
from typing import Optional
from pydantic import BaseModel
from src.schemas.constants import PurchaseStatus


class Purchase(BaseModel):
    code: str
    date: date
    value: float
    cpf: str
    status: Optional[PurchaseStatus] = PurchaseStatus.VALIDATION
