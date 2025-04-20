import requests
from http.server import HTTPServer
from callback_handler import CallbackHandler
from utils import redirect_to_auth_url
import curlify
import os

class GithubAPIClient:
    def __init__(self):
        self.BASE_URL = "https://api.appmetrica.yandex.ru/management/v1/applications"
        self.auth_token = None

    def make_request(self, method, url, requires_auth=False, **kwargs):

        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if requires_auth == True:
            try:
                with open('token.json', 'r') as f:  # Читаем токен из файла
                    auth_token = f.read().strip()
            except FileNotFoundError:
                print('файл токена не найден!')
                self.authenticate()  # Если файла нет, вызываем аутентификацию
                return self.make_request(method, url, requires_auth, **kwargs)

            headers['Authorization'] = f'OAuth  {auth_token[1:-1]}'

        response = requests.request(method, url, headers=headers, **kwargs)
        
        print("Status Code:", response.status_code)  # Код статуса (200, 404 и т.д.)
        print("Headers:", response.headers)         # Заголовки ответа
        print("Body (text):", response.text)       # Тело ответа в виде текста

        if response.status_code == 401:
            print("Token doesn't fit. Re-authenticating...")
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
    
    def get_apps_list(self):
        apps_list = self.make_request('GET', self.BASE_URL, requires_auth=True)
        return apps_list
    
    def create_app(self, app_obj):
        new_app = self.make_request('POST', self.BASE_URL, requires_auth=True, json=app_obj.to_dict())
        return new_app
    
    def update_app(self, app_id, app_obj):
        url = f'{self.BASE_URL[:-1]}/{app_id}'
        new_app = self.make_request('PUT', url, requires_auth=True, json=app_obj.to_dict())
        return new_app
    
    def delete_app(self, app_id):
        url = f'{self.BASE_URL[:-1]}/{app_id}'
        new_app = self.make_request('DELETE', url, requires_auth=True)
        return new_app
