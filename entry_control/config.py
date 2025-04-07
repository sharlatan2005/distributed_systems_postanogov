from sqlalchemy.engine import URL

SQLITE_CONFIG = {
    'database': 'path/to/source.db'
}

POSTGRES_CONFIG = URL.create(
    drivername='postgresql+psycopg2',
    username='user',
    password='pass',
    host='localhost',
    port=5432,
    database='target_db'
)