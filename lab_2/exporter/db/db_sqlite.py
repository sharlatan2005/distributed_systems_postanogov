from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pathlib import Path
from config import SQLITE_PATH

db_path = Path(__file__).parent.parent / SQLITE_PATH 
engine = create_engine(f'sqlite:///{SQLITE_PATH}', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()