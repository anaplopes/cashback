from fastapi import APIRouter, status
from src.entities.dealer import Dealer


dealer_router = APIRouter(prefix="/v1/cashback/dealer", tags=["dealer"])


@dealer_router.post(
    "/register", response_model=Dealer, status_code=status.HTTP_201_CREATED
)
async def register_dealer(dealer: Dealer):
    """
    Rota para cadastra um novo revendedor(a):

    - **name**: nome do revendedor(a)
    - **cpf**: cpf do revendedor(a)
    - **auth.email**: email do revendedor(a)
    - **auth.password**: senha do revendedor(a)
    """
    return dealer
