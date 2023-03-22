import uuid
from src.infra.database import Base
from sqlalchemy import Column, String, Float, Date
from sqlalchemy.dialects.postgresql import UUID


class PurchaseModel(Base):
    __tablename__ = "purchase"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)
    cpf = Column(String(11), nullable=False)
    status = Column(String(50), nullable=False)
