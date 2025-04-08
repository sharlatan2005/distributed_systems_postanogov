from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_sqlite_session(sqlite_path):
    engine = create_engine(f'sqlite:///{sqlite_path}')
    Session = sessionmaker(bind=engine)
    return Session()

def create_postgres_session(config, base):
    engine = create_engine(config)
    base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()