import base64
from src.schemas.constant import Output
from src.schemas.reseller import Reseller
from src.models.reseller import ResellerModel
from fastapi import Depends, status, HTTPException
from src.repositories.reseller import ResellerRepository


class ResellerUseCase:
    def __init__(self, repository: ResellerRepository = Depends()) -> None:
        self.repository = repository

    def pwd_hash(self, password: str) -> base64:
        return base64.b64encode(password.encode()).decode()

    async def create(self, reseller: Reseller) -> Output | HTTPException:
        record = self.repository.filter_by_cpf(cpf=reseller.cpf)
        if record:
            raise HTTPException(
                detail="Reseller already registered",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        data = self.repository.add(
            reseller=ResellerModel(
                name=reseller.name,
                cpf=reseller.cpf,
                email=reseller.email,
                password=self.pwd_hash(reseller.password),
            )
        )
        return Output(
            data=[{"id": data.id}],
            message="Reseller successfully registered",
            statusCode=status.HTTP_201_CREATED,
        )
