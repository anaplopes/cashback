from fastapi import Depends
from sqlalchemy.orm import Session
from src.models.purchase import PurchaseModel
from src.infra.database.connection import db_connection


class PurchaseRepository:
    def __init__(self, db: Session = Depends(db_connection)) -> None:
        self.db = db

    def add(self, purchase: PurchaseModel) -> PurchaseModel:
        self.db.add(purchase)
        self.db.commit()
        self.db.refresh(purchase)
        return purchase

    def filter_by_cpf(self, cpf: str) -> PurchaseModel:
        return self.db.query(PurchaseModel).filter_by(cpf=cpf).all()

    def filter_by_code(self, code: str) -> PurchaseModel:
        return self.db.query(PurchaseModel).filter_by(code=code).first()
