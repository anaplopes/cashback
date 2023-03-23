from sqlalchemy.ext.declarative import declarative_base
from src.infra.database.connection import engine


Base = declarative_base()


def init():
    Base.metadata.create_all(engine())
