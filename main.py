import tomli
from enum import Enum
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from typing import List


app = FastAPI()
started_date = datetime.now()


class Status(str, Enum):
    VALIDATION = "Em validação"
    APPROVED = "Aprovado"


class Auth(BaseModel):
    email: str
    password: str


class Dealer(BaseModel):
    name: str
    cpf: str
    auth: Auth


class Purchase(BaseModel):
    code: str
    date: str
    value: float
    cpf: str
    status: Status


def bonus(sum_purchase: float) -> int:
    if sum_purchase <= 1000.0:
        return 10

    if sum_purchase > 1000.0 and sum_purchase <= 1500.0:
        return 15

    if sum_purchase > 1500.0:
        return 20


def cashback_purchase(rows: List[Purchase]) -> List[Purchase]:
    sum_purchase: float = sum([row.value for row in rows])
    cashback: int = bonus(sum_purchase=sum_purchase)

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


@app.get("/api/v1/cashback/health")
async def health_check():
    with open("pyproject.toml", mode="rb") as tm:
        config = tomli.load(tm)
        cfg = config["tool"]["poetry"]

        response = {
            "code": 200,
            "status": "Healthy",
            "name": cfg["name"],
            "version": cfg["version"],
            "started": started_date.strftime("%b %d %Y %H:%M:%S"),
            "uptime": str(datetime.now() - started_date),
        }
        return response


@app.post("/api/v1/cashback/auth")
async def validate_auth(auth: Auth):
    return


@app.post("/api/v1/cashback/register/dealer")
async def register_dealer(dealer: Dealer):
    return dealer


@app.post("/api/v1/cashback/register/purchase")
async def register_purchase(purchase: Purchase):
    purchase.update(
        {
            "status": Status.APPROVED
            if purchase.cpf == "15350946056"
            else Status.VALIDATION
        }
    )
    return purchase


@app.get("/api/v1/cashback/list/purchases/{cpf}")
async def list_purchases(cpf: str):
    rows = None  # TODO filtrar todas as compras do mês
    return cashback_purchase(rows=rows)


@app.get("/api/v1/cashback/full/{cpf}")
async def full_cashback(cpf: str):
    return cpf
