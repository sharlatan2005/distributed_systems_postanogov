import requests
from http.server import HTTPServer
from callback_handler import CallbackHandler
from utils import redirect_to_auth_url, is_protected_endpoint
from requests_oauthlib import OAuth2Session
from config import CLIENT_ID, CLIENT_SECRET, CODE_FOR_TOKEN_URL, AUTH_URL, REDIRECT_URL
import json
import os 

class GithubAPIClient:
    def __init__(self):
        self.BASE_URL = "https://api.github.com/repos"
        self.auth_token = None

    def make_request(self, method, url, requires_auth=False, **kwargs):
        # Читаем токен из файла
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if kwargs.get('requires_auth') == True:
            try:
                with open('token.json', 'r') as f:
                    auth_token = f.read().strip()
            except FileNotFoundError:
                print('файл токена не найден!')
                self.authenticate()  # Если файла нет, вызываем аутентификацию
                return self.make_request(method, url, requires_auth, **kwargs)

            headers['Authorization'] = f'Bearer {auth_token}'

        response = requests.request(method, url, headers=headers, **kwargs)

        if response.status_code == 403:
            print("Token expired. Re-authenticating...")
            os.remove('token.json')  # Удаляем невалидный токен
            self.authenticate()     # Запрашиваем новый токен
            return self.make_request(method, url, requires_auth, **kwargs)

        response.raise_for_status()
        return response.json() if response.content else None

    def authenticate(self):
        """Запускает OAuth-поток, если токена нет."""

        redirect_to_auth_url()
        
        server = HTTPServer(("localhost", 8000), CallbackHandler)        
        print("Waiting for authentication...")
        server.handle_request()       
    
    def get_repo(self, repo_owner_name, repo_name):
        url = f'{self.BASE_URL}/{repo_owner_name}/{repo_name}'
        repo_data = self.make_request('GET', url)
        return repo_data['id']
    
    def update_repo(self, repo_owner_name, repo_name, new_repo_obj):
        url = f'{self.BASE_URL}/{repo_owner_name}/{repo_name}'
        repo_data = self.make_request('PATCH', url, True, json=new_repo_obj)
        return repo_data['id']

    