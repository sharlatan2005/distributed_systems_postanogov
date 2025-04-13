import requests
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler
from config import CLIENT_ID, CLIENT_SECRET, CODE_FOR_TOKEN_URL


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
            # Получаем доступ к github_client через server
            self.server.github_client.auth_token = token
            self.server.github_client.auth_event.set()  # Оповещаем о получении токена
        else:
            self.send_error(400, "Code not found")

    def exchange_code_for_token(self, code):
        response = requests.post(
            CODE_FOR_TOKEN_URL,
            params={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": code,
            },
            headers={"Accept": "application/json"},
        )
        return response.json().get("access_token")