from os import getenv
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID=getenv('CLIENT_ID')
CLIENT_SECRET=getenv('CLIENT_SECRET')
AUTH_URL = getenv('AUTH_URL')
REDIRECT_URL=getenv('REDIRECT_URL')
CODE_FOR_TOKEN_URL = getenv('CODE_FOR_TOKEN_URL')