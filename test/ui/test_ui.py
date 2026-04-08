import allure
import pytest
import config
from selenium.webdriver.common.by import By

from page.Create_new_repository import CreateNewRepository
from page.Delete_page import DeletePage


@allure.epic("GitHub Web Application")
@pytest.mark.ui
class TestGitHub:
    @allure.title("Создание репозитория: без имени (негативный)")
    @allure.feature("Создание репозитория")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_no_name(self, logged_in_browser):
        with allure.step("Перейти на страницу создания"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            url_before = logged_in_browser.current_url
        with allure.step("Попытаться нажать кнопку создания"):
            btn_xpath = "//button[contains(., 'Create repository')]"
            logged_in_browser.find_element(By.XPATH, btn_xpath).click()
        with allure.step("Убедиться, что репозиторий не создан"):
            assert logged_in_browser.current_url == url_before
            assert "Name cannot be blank" in logged_in_browser.page_source

    @allure.title("Создание репозитория: имя из одного символа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_repository_minimal_length(self, logged_in_browser):
        name = config.UI_REPO_NAME_1
        full_name = config.FULL_UI_REPO_1
        with allure.step(f"Создание репозитория: {name}"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            CreateNewRepository(logged_in_browser).create_repo(name)
        with allure.step(f"Удаление репозитория: {full_name}"):
            delete_page = DeletePage(logged_in_browser)
            delete_page.delete_repository(full_name)

    @allure.title("Создание репозитория: имя из двух символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_repository_two_character_repo(self, logged_in_browser):
        name = config.UI_REPO_NAME_2
        full_name = config.FULL_UI_REPO_2
        with allure.step(f"Создание репозитория: {name}"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            CreateNewRepository(logged_in_browser).create_repo(name)
        with allure.step(f"Удаление репозитория: {full_name}"):
            delete_page = DeletePage(logged_in_browser)
            delete_page.delete_repository(full_name)

    @allure.title("Создание репозитория: имя из 50 символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_repository_50_symbols(self, logged_in_browser):
        name = config.UI_REPO_NAME_3
        full_name = config.FULL_UI_REPO_3
        with allure.step(f"Создание репозитория: {name}"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            CreateNewRepository(logged_in_browser).create_repo(name)
        with allure.step(f"Удаление репозитория: {full_name}"):
            delete_page = DeletePage(logged_in_browser)
            delete_page.delete_repository(full_name)

    @allure.title("Удаление репозитория: в поле Repository name - цифры")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_repository_numeric(self, logged_in_browser):
        name = config.UI_REPO_NAME_4
        full_name = config.FULL_UI_REPO_4
        with allure.step(f"Создание репозитория: {name}"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            CreateNewRepository(logged_in_browser).create_repo(name)
        with allure.step(f"Удаление репозитория: {full_name}"):
            delete_page = DeletePage(logged_in_browser)
            delete_page.delete_repository(full_name)

    @allure.title("Создание репозитория: смешанный регистр")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_repository_lifecycle_mixed_register(self, logged_in_browser):
        name = config.UI_REPO_NAME_5
        full_name = config.FULL_UI_REPO_5
        with allure.step(f"Создание репозитория: {name}"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            CreateNewRepository(logged_in_browser).create_repo(name)
        with allure.step(f"Удаление репозитория: {full_name}"):
            delete_page = DeletePage(logged_in_browser)
            delete_page.delete_repository(full_name)

    @allure.title("Создание репозитория: имя в верхнем регистре")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_repository_uppercase_repo(self, logged_in_browser):
        name = config.UI_REPO_NAME_6
        full_name = config.FULL_UI_REPO_6
        with allure.step(f"Создание репозитория: {name}"):
            logged_in_browser.get(config.GITHUB_NEW_REPO_URL)
            CreateNewRepository(logged_in_browser).create_repo(name)
        with allure.step(f"Удаление репозитория: {full_name}"):
            delete_page = DeletePage(logged_in_browser)
            delete_page.delete_repository(full_name)
