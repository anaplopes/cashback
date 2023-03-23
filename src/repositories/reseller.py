from fastapi import Depends
from sqlalchemy.orm import Session
from src.models.reseller import ResellerModel
from src.infra.database.connection import db_connection


class ResellerRepository:
    def __init__(self, db: Session = Depends(db_connection)) -> None:
        self.db = db

    def add(self, reseller: ResellerModel) -> ResellerModel:
        self.db.add(reseller)
        self.db.commit()
        self.db.refresh(reseller)
        return reseller

    def filter_by_email(self, email: str) -> ResellerModel:
        return self.db.query(ResellerModel).filter_by(email=email).first()

    def filter_by_cpf(self, cpf: str) -> ResellerModel:
        return self.db.query(ResellerModel).filter_by(cpf=cpf).first()
