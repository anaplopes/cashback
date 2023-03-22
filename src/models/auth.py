import uuid
from src.infra.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class AuthModel(Base):
    __tablename__ = "auth"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
