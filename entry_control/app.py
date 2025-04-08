from config import SQLITE_PATH, POSTGRES_CONFIG
from db_utils import create_sqlite_session, create_postgres_session
from models.target.base import Base as TargetBase
from normalizer import Normalizer

def main():
    sqlite_session = create_sqlite_session(SQLITE_PATH)

    postgres_session = create_postgres_session(POSTGRES_CONFIG, TargetBase)
    
    normalizer = Normalizer(sqlite_session, postgres_session)
    normalizer.normalize()

if __name__ == '__main__':
    main()