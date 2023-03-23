import uuid
from sqlalchemy.sql import func
from src.models.base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Float, Date, DateTime


class PurchaseModel(Base):
    __tablename__ = "purchase"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String(100), nullable=False, unique=True)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)
    cpf = Column(String(11), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
