import requests
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler
from config import CODE_FOR_TOKEN_URL, BASIC_TOKEN
import json
import curlify


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        code = params.get("code", [None])[0]

        if code:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Auth success! You can close this tab.")
            
            token = self.exchange_code_for_token(code)
            with open("token.json", "w") as f:
                json.dump(token, f)
                print(f'Токен: {token}')
            print("Token saved to token.json!")
        else:
            self.send_error(400, "Code not found")


    def exchange_code_for_token(self, code):
        response = requests.post(
            CODE_FOR_TOKEN_URL,
            headers={
                'Content-type': 'application/x-www-form-urlencoded',
                'Authorization': f'Basic {BASIC_TOKEN}' 
            },
            data={
                "grant_type": "authorization_code",
                "code": code
            },
        )
        print(curlify.to_curl(response.request))

        return response.json().get("access_token")