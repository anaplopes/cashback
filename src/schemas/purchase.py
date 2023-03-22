from enum import Enum
from datetime import date
from typing import Optional
from pydantic import BaseModel


class PurchaseStatus(str, Enum):
    VALIDATION = "Em validação"
    APPROVED = "Aprovado"


class Purchase(BaseModel):
    code: str
    date: date
    value: float
    cpf: str
    status: Optional[PurchaseStatus] = PurchaseStatus.VALIDATION
