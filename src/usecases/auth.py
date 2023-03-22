from src.schemas.auth import Auth
from fastapi import HTTPException, status


class AuthUseCase:
    async def validate(self, auth: Auth):
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

        return "JWT"
