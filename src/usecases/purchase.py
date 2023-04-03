from typing import List, Dict
from src.schemas.constant import Output
from src.models.purchase import PurchaseModel
from src.schemas.constant import PurchaseStatus
from fastapi import Depends, status, HTTPException
from src.repositories.purchase import PurchaseRepository
from src.schemas.purchase import Purchase, PurchaseSchema


class PurchaseUseCase:
    def __init__(self, repository: PurchaseRepository = Depends()) -> None:
        self.repository = repository

    def __bonus(self, sum_purchase: float) -> int:
        if sum_purchase <= 1000.0:
            return 10

        if sum_purchase > 1000.0 and sum_purchase <= 1500.0:
            return 15

        if sum_purchase > 1500.0:
            return 20

    def sum_purchase(self, rows: List[PurchaseSchema]) -> Dict[int, float]:
        purchase_month = {}
        for purchase in rows:
            month_purchase = purchase.date.month

            if month_purchase in purchase_month:
                purchase_month[month_purchase] += purchase.value
            else:
                purchase_month[month_purchase] = purchase.value

        return purchase_month

    def calc_cashback(self, rows: List[PurchaseSchema]) -> List[PurchaseSchema]:
        sum_purchase_month = self.sum_purchase(rows=rows)
        for row in rows:
            month_purchase = row.date.month
            cashback: int = self.__bonus(
                sum_purchase=sum_purchase_month[month_purchase]
            )
            row.val_cashback = round(row.value * (cashback / 100), 2)
            row.per_cashback = round(
                (row.val_cashback / sum_purchase_month[month_purchase]) * 100, 2
            )
        return rows

    async def find(self, cpf: str) -> Output | HTTPException:
        records = self.repository.filter_by_cpf(cpf=cpf)
        if not records:
            raise HTTPException(
                detail="No purchase found", status_code=status.HTTP_404_NOT_FOUND
            )

        return Output(
            data=self.calc_cashback(rows=records),
            message="OK",
            statusCode=status.HTTP_200_OK,
        )

    async def create(self, purchase: Purchase) -> Output | HTTPException:
        record = self.repository.filter_by_code(code=purchase.code)
        if record:
            raise HTTPException(
                detail="Purchase already registered",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        data = self.repository.add(
            purchase=PurchaseModel(
                code=purchase.code,
                date=purchase.date,
                value=purchase.value,
                cpf=purchase.cpf,
                status=PurchaseStatus.APPROVED
                if purchase.cpf == "15350946056"
                else PurchaseStatus.VALIDATION,
            )
        )
        return Output(
            data=[{"id": data.id}],
            message="Successfully registered purchase",
            statusCode=status.HTTP_201_CREATED,
        )
