from src.schemas.reseller import Reseller
from fastapi import APIRouter, Depends, status
from src.usecases.reseller import ResellerUseCase


reseller_router = APIRouter(prefix="/reseller", tags=["reseller"])


@reseller_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_reseller(reseller: Reseller, service: ResellerUseCase = Depends()):
    """
    Rota para cadastra um novo revendedor(a):

    - **name**: nome do revendedor(a)
    - **cpf**: cpf do revendedor(a)
    - **email**: email do revendedor(a)
    - **password**: senha do revendedor(a)
    """
    return await service.create(reseller=reseller)
