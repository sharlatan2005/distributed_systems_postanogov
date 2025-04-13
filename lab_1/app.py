from api_client import GithubAPIClient

if __name__ == "__main__":
    app = GithubAPIClient()

    print('Запрашиваем репозиторий и выводим его айди')
    app.get_repo('sharlatan2005', 'TodoList')

    
