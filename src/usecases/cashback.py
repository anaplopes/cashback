import json
from typing import Any
from src.infra.boticario.client import BoticarioClient
from src.infra.boticario.exceptions import BoticarioException, BoticarioRequestException


class CashbackUseCase:
    def __init__(self) -> None:
        self.boticario_client = BoticarioClient()

    async def get(self, cpf: str) -> Any:
        try:
            send = self.boticario_client.get_cashback(cpf=cpf)
            return json.loads(send.response)
        except BoticarioRequestException or BoticarioException as e:
            return f"BoticarioError: {e.error} - {e.message}"
