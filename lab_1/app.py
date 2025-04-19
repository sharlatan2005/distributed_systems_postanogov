from api_client import GithubAPIClient
from repo import Repo
def main():
    api_client = GithubAPIClient()

    # print(api_client.get_repo('sharlatan2005', 'TodoList'))

    repo = Repo('Fifka')
    print(api_client.update_repo('sharlatan2005', 'TodoList', repo))


if __name__ == '__main__':
    main()