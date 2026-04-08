import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from page.Main_page import MainPage
from page.Login_page import LoginPage
from api.RepoApi import RepoApi
import config


@pytest.fixture(scope="function")
def browser():
    with allure.step("Открыть и настроить браузер"):
        service = Service(ChromeDriverManager().install())
        browser_instance: WebDriver = webdriver.Chrome(service=service)
        browser_instance.maximize_window()
        browser_instance.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
        browser_instance.implicitly_wait(config.IMPLICIT_WAIT)
    yield browser_instance
    with allure.step("Закрыть браузер"):
        browser_instance.quit()


@pytest.fixture(scope="function")
def logged_in_browser(browser):
    with allure.step("Выполнение входа в систему (авторизация)"):
        main_page = MainPage(browser)
        main_page.go_to_login()
        login_page = LoginPage(browser)
        login_page.login_as(config.USERNAME, config.PASSWORD)
        WebDriverWait(browser, 10).until(
            EC.url_changes(config.GITHUB_URL + "/login"))
    return browser


@pytest.fixture(scope="function")
def repo_api():
    with allure.step("Инициализация API клиента GitHub"):
        api = RepoApi()
        allure.attach(api.base_url, name="API Base URL",
                      attachment_type=allure.attachment_type.TEXT)
        return api


@pytest.fixture(scope="function")
def bad_repo_api():
    with allure.step("Инициализация API клиента с неверным токеном"):
        api = RepoApi(token="invalid_token_123456789")
        return api


@pytest.fixture(scope="function")
def repo_manager(repo_api):
    repos_to_cleanup = []

    def _create(name):
        if name not in repos_to_cleanup:
            repos_to_cleanup.append(name)
        repo_api.delete_repository(name)
        import time
        time.sleep(1)
        resp = repo_api.create_repository(name)
        return resp
    yield _create
    for name in repos_to_cleanup:
        import time
        time.sleep(2)
        for attempt in range(5):
            with allure.step(
                 f"Cleanup: Попытка удаления {name} #{attempt + 1}"):
                resp = repo_api.delete_repository(name)
                if resp.status_code in [204, 404]:
                    break
                time.sleep(3)
