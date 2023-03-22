from typing import List
from src.schemas.purchase import Purchase
from src.schemas.constants import PurchaseStatus


class PurchaseUseCase:
    async def _bonus(self, sum_purchase: float) -> int:
        if sum_purchase <= 1000.0:
            return 10

        if sum_purchase > 1000.0 and sum_purchase <= 1500.0:
            return 15

        if sum_purchase > 1500.0:
            return 20

    async def _calc_cashback(self, rows: List[Purchase]) -> List[Purchase]:
        sum_purchase: float = sum([row.value for row in rows])
        cashback: int = self._bonus(sum_purchase=sum_purchase)

        for row in rows:
            val_cashback = round(row.value * (cashback / 100), 2)
            per_cashback = round((val_cashback / sum_purchase) * 100, 2)
            row.update(
                {
                    "per_cashback": per_cashback,
                    "val_cashback": val_cashback,
                }
            )
        return rows

    async def find(self, cpf: str) -> List[Purchase]:
        rows = None  # TODO filtrar todas as compras do mês
        return self._calc_cashback(rows=rows)

    async def create(self, purchase: Purchase):
        if purchase.cpf == "15350946056":
            purchase.status = PurchaseStatus.APPROVED
        # TODO inserir na tabela purchase
        return "Successfully registered purchase"
