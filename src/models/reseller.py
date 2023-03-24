import uuid
from sqlalchemy.sql import func
from src.infra.database.modelbase import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime


class ResellerModel(Base):
    __tablename__ = "reseller"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
