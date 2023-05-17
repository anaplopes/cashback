import base64
from log_config import logger
from src.schemas.reseller import Auth
from src.schemas.constant import Output
from fastapi import Depends, status, HTTPException
from src.repositories.reseller import ResellerRepository


class AuthUseCase:
    def __init__(self, repository: ResellerRepository = Depends()) -> None:
        self.repository = repository

    async def validate(self, auth: Auth) -> Output | HTTPException:
        user = self.repository.filter_by_email(email=auth.email)
        if not user:
            logger.info("Unregistered user")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Unregistered user"
            )

        pwd_hash = user.password
        pwd_str = base64.b64decode(pwd_hash.encode()).decode()
        verify_pwd = True if pwd_str == auth.password else False
        if verify_pwd is False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
            )

        return Output(message="Authorized user", statusCode=status.HTTP_200_OK)
