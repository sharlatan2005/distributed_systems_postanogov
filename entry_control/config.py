from sqlalchemy.engine import URL

from os import getenv
from dotenv import load_dotenv

load_dotenv()

SQLITE_PATH = getenv('SQLITE_DB_PATH')

POSTGRES_CONFIG = URL.create(
    drivername='postgresql+psycopg2',
    username=getenv('PG_DB_USER'),
    password=getenv('PG_DB_PASS'),
    host=getenv('PG_DB_HOST'),
    port=getenv('PG_DB_PORT'),
    database=getenv('PG_DB_NAME')
)
