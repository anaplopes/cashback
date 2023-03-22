from sqlalchemy.orm import Session
from src.models.reseller import ResellerModel


class ResellerRepository:
    @staticmethod
    def save(db: Session, reseller: ResellerModel):
        db.add(reseller)
        db.commit()
        return reseller

    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(ResellerModel).filter(ResellerModel.id == id).first()
