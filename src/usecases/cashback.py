import json
from fastapi import Depends, status
from src.schemas.constant import Output
from src.infra.boticario.client import BoticarioClient
from src.infra.boticario.exceptions import BoticarioException, BoticarioRequestException


class CashbackUseCase:
    def __init__(self, boticario_client: BoticarioClient = Depends()) -> None:
        self.boticario_client = boticario_client

    async def get(self, cpf: str) -> Output:
        try:
            send = self.boticario_client.get_cashback(cpf=cpf)
            data = json.loads(send.response)
            return Output(
                data=[{"credit": data["body"]["credit"]}],
                message="OK",
                statusCode=status.HTTP_200_OK,
            )
        except BoticarioRequestException or BoticarioException as e:
            return Output(message=e.message, error=e.error, statusCode=e.status_code)
