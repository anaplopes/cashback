from enum import Enum
from pydantic import BaseModel
from typing import List, Optional, Any


class PurchaseStatus(str, Enum):
    VALIDATION = "Em validação"
    APPROVED = "Aprovado"


class Output(BaseModel):
    data: Optional[List[Any]] = []
    message: str
    error: Optional[str] = None
    statusCode: int
