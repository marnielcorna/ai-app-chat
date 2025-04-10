from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db_settings import build_db_url


class Database:
    def __init__(self):
        self.engine = create_engine(build_db_url())
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()
