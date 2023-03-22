from src.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infra.database.exceptions import DbException


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Connection:
    def __init__(self):
        self.url_engine = settings.DB_URL
        self.engine = None
        self._session = None

    def create_connection(self):
        self.engine = create_engine(self.url_engine, convert_unicode=True)
        session = sessionmaker(bind=self.engine, expire_on_commit=False)
        self._session = session()
        return self._session

    def save_change(self):
        try:
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise DbException(message=str(e))
        finally:
            self._session.close()
            self.engine.dispose()
