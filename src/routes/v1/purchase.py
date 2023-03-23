from src.schemas.purchase import Purchase
from fastapi import APIRouter, Depends, status
from src.usecases.purchase import PurchaseUseCase


purchase_router = APIRouter(prefix="/purchase", tags=["purchase"])


@purchase_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_purchase(purchase: Purchase, service: PurchaseUseCase = Depends()):
    """
    Rota para cadastra uma nova compra:

    - **code**: código da compra
    - **date**: data da compra
    - **value**: valor da compra
    - **cpf**: cpf do revendedor(a)
    """
    return await service.create(purchase=purchase)


@purchase_router.get("/list/{cpf}")
async def list_purchases(cpf: str, service: PurchaseUseCase = Depends()):
    """
    Rota para retornar compras cadastradas:

    - **cpf**: cpf do revendedor(a)
    """
    return await service.find(cpf=cpf)
