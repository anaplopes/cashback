from src.schemas.reseller import Reseller
from src.repositories.reseller import ResellerRepository


class ResellerUseCase:
    def __init__(self) -> None:
        self.repository = ResellerRepository

    async def create(self, reseller: Reseller):
        # TODO inserir na tabela reseller
        self.repository.save(reseller=reseller)
        return "Reseller successfully registered"
