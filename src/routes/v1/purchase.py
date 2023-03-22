from typing import List
from fastapi import APIRouter, Depends, status
from src.schemas.purchase import Purchase
from src.usecases.purchase import PurchaseUseCase


purchase_router = APIRouter(prefix="/purchase", tags=["purchase"])


@purchase_router.post(
    "/register", response_model=Purchase, status_code=status.HTTP_201_CREATED
)
async def register_purchase(purchase: Purchase, service: PurchaseUseCase = Depends()):
    """
    Rota para cadastra uma nova compra:

    - **code**: código da compra
    - **date**: data da compra
    - **value**: valor da compra
    - **cpf**: cpf do revendedor(a)
    """
    return await service.create_purchase(purchase=purchase)


@purchase_router.get("/list/{cpf}", response_model=List[Purchase])
async def list_purchases(cpf: str, service: PurchaseUseCase = Depends()):
    """
    Rota para retornar compras cadastradas:

    - **cpf**: cpf do revendedor(a)
    """
    return await service.find(cpf=cpf)
