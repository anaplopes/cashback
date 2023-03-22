import uuid
from src.infra.database.client import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class ResellerModel(Base):
    __tablename__ = "reseller"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
