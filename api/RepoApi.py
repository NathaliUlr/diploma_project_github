import requests
import config
import allure


class RepoApi:
    def __init__(self, token=None):
        self.base_url = config.GITHUB_API_URL
        self.user_login = config.USERNAME
        self.token = token if token is not None else config.GITHUB_TOKEN

    @allure.step(
            "API: Получение списка репозиториев пользователя: {user_login}")
    def get_user_repositories(self, user_login: str):
        path = f"{self.base_url}/users/{user_login}/repos"
        resp = requests.get(path)
        return resp

    @allure.step("API: Создание репозитория с именем: {name}")
    def create_repository(self, name: str):
        header = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }
        body = {"name": name}
        path = f"{self.base_url}/user/repos"
        resp = requests.post(path, json=body, headers=header)
        return resp

    @allure.step("API: Удаление репозитория: {name}")
    def delete_repository(self, name: str):
        header = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }
        path = f"{self.base_url}/repos/{self.user_login}/{name}"
        resp = requests.delete(path, headers=header)
        return resp

    @allure.step(
            "API: Редактирование репозитория {name}: "
            "новое описание '{description}'")
    def edit_repository(self, name: str, description: str):
        header = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"}
        body = {
            'name': name,
            'description': description}
        path = f"{self.base_url}/repos/{self.user_login}/{name}"
        resp = requests.patch(path, json=body, headers=header)
        return resp
