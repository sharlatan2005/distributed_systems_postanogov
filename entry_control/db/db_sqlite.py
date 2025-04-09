from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLITE_PATH

engine = create_engine(f'sqlite:///{SQLITE_PATH}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()