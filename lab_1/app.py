from api_client import GithubAPIClient
from models import App

def main():
    api_client = GithubAPIClient()

    print(api_client.get_apps_list())

    app = App('Very cool app')
    new_app = api_client.create_app(app)

    new_app_id = new_app['application']['id']

    app.name = 'Very very cool app'
    api_client.update_app(new_app_id, app)

    api_client.delete_app(4733470)

if __name__ == '__main__':
    main()