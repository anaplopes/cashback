from typing import List
from src.entities.purchase import Purchase


class Cashback:
    def bonus(self, sum_purchase: float) -> int:
        if sum_purchase <= 1000.0:
            return 10

        if sum_purchase > 1000.0 and sum_purchase <= 1500.0:
            return 15

        if sum_purchase > 1500.0:
            return 20

    def cashback_purchase(self, rows: List[Purchase]) -> List[Purchase]:
        sum_purchase: float = sum([row.value for row in rows])
        cashback: int = self.bonus(sum_purchase=sum_purchase)

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
