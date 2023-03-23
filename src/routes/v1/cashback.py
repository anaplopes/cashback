from fastapi import APIRouter, Depends
from src.usecases.cashback import CashbackUseCase


cashback_router = APIRouter(prefix="/cashback", tags=["cashback"])


@cashback_router.get("/{cpf}")
async def full_cashback(cpf: str, service: CashbackUseCase = Depends()):
    """
    Rota para retornar o acumulado de cashback:

    - **cpf**: cpf do revendedor(a)
    """
    return await service.get(cpf=cpf)
