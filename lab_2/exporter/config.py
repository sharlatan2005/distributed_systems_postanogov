from os import getenv
from dotenv import load_dotenv

load_dotenv()

SQLITE_PATH = getenv('SQLITE_DB_PATH')
