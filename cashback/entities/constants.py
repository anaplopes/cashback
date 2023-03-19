from enum import Enum


class PurchaseStatus(str, Enum):
    VALIDATION = "Em validação"
    APPROVED = "Aprovado"
