from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, Any


class PurchaseStatus(str, Enum):
    VALIDATION = "Em validação"
    APPROVED = "Aprovado"


class Output(BaseModel):
    data: Optional[List[Any]] = Field(default_factory=list)
    message: str
    error: Optional[str] = None
    statusCode: int
