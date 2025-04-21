from api_client import GithubAPIClient
from models import App

def main():
    api_client = GithubAPIClient()

    print(api_client.get_apps_list()) # read 

    # app = App('Very cool app')
    # new_app = api_client.create_app(app) # create 

    # new_app_id = new_app['application']['id']

    # app.name = 'Very very cool app'
    # api_client.update_app(new_app_id, app) # update

    # api_client.delete_app(new_app_id) # delete

if __name__ == '__main__':
    main()