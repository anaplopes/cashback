from src.schemas.auth import Auth
from fastapi import APIRouter, Depends
from src.usecases.auth import AuthUseCase


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/")
async def authenticate(auth: Auth, service: AuthUseCase = Depends()):
    """
    Rota para validar um login de um revendedor(a):

    - **email**: email do revendedor
    - **password**: senha do revendedor
    """
    return await service.validate(auth=auth)
