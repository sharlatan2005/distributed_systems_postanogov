import requests
from threading import Event
from http.server import HTTPServer
from callback_handler import CallbackHandler
from utils import redirect_to_auth_url

from threading import Event

class GithubAPIClient:
    def __init__(self):
        self.BASE_URL = "https://api.github.com/repos"
        self.auth_token = None
        self.auth_event = Event()
    
    def make_request(self, method, url, **kwargs):
        if not self.auth_token:
            self.authenticate()

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.auth_token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        response = requests.request(method, url, headers=headers, **kwargs)

        if response.status_code == 401:
            print("Token expired. Re-authenticating...")
            self.auth_token = None
            return self.make_request(method, url, **kwargs)

        response.raise_for_status()
        return response.json() if response.content else None

    def authenticate(self):
        """Запускает OAuth-поток, если токена нет."""
        server = HTTPServer(("localhost", 8000), CallbackHandler)
        server.github_client = self  # Передаем текущий экземпляр клиента
        
        redirect_to_auth_url()
        
        self.auth_event.clear()
        print("Waiting for authentication...")
        self.auth_event.wait()  # Ждем получения токена
        server.shutdown()
        print("Authentication complete")
    
    def get_repo(self, repo_owner_name, repo_name):
        url = f'{self.BASE_URL}/{repo_owner_name}/{repo_name}'
        repo_data = self.make_request('GET', url)
        return repo_data['id']
