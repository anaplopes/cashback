from fastapi import APIRouter, HTTPException, status
from src.entities.auth import Auth


auth_router = APIRouter(prefix="/v1/cashback/auth", tags=["auth"])


@auth_router.post("/")
async def validate_auth(auth: Auth):
    """
    Rota para validar um login de um revendedor(a):

    - **email**: email do revendedor
    - **password**: senha do revendedor
    """
    # TODO filtrar revendedor pelo email
    # TODO validar a senha
    # TODO se a senha esta correta retorna o jwt
    # TODO se a senha não esta correta retorna status não autorizado
    user = auth
    password = False
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User does not exist"
        )

    if user and password is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
        )

    return {"message": "TOKEN"}
