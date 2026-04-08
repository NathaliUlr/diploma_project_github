import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
import config


class LoginPage(BasePage):
    _USER_FIELD = (By.ID, "login_field")
    _PASS_FIELD = (By.ID, "password")
    _SUBMIT_BTN = (By.NAME, "commit")

    @allure.step("Открыть страницу авторизации GitHub")
    def open_login_page(self):
        self.driver.get(config.GITHUB_LOGIN_URL)

    @allure.step("Ввести логин: {username}")
    def enter_username(self, username):
        self.driver.find_element(*self._USER_FIELD).send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.driver.find_element(*self._PASS_FIELD).send_keys(password)

    @allure.step("Нажать кнопку 'Sign in'")
    def click_submit_button(self):
        self.driver.find_element(*self._SUBMIT_BTN).click()

    @allure.step("Процесс авторизации пользователя {username}")
    def login_as(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()
