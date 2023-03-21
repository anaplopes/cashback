from typing import List
from fastapi import APIRouter, status
from src.entities.purchase import Purchase
from src.entities.constants import PurchaseStatus
from src.usecases.cashback import cashback_purchase


purchase_router = APIRouter(prefix="/v1/cashback/purchase", tags=["purchase"])


@purchase_router.post(
    "/register", response_model=Purchase, status_code=status.HTTP_201_CREATED
)
async def register_purchase(purchase: Purchase):
    """
    Rota para cadastra uma nova compra:

    - **code**: código da compra
    - **date**: data da compra
    - **value**: valor da compra
    - **cpf**: cpf do revendedor(a)
    """
    if purchase.cpf == "15350946056":
        purchase.status = PurchaseStatus.APPROVED
    return purchase


@purchase_router.get("/list/{cpf}", response_model=List[Purchase])
async def list_purchases(cpf: str):
    """
    Rota para retornar compras cadastradas:

    - **cpf**: cpf do revendedor(a)
    """
    rows = None  # TODO filtrar todas as compras do mês
    return cashback_purchase(rows=rows)
