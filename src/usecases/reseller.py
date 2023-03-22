from src.schemas.reseller import Reseller


class ResellerUseCase:
    async def create(self, reseller: Reseller):
        # TODO inserir na tabela reseller
        return "Reseller successfully registered"
