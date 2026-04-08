import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import config


class MainPage(BasePage):
    _URL = config.GITHUB_URL
    _SIGN_IN_BTN = (By.CSS_SELECTOR, "a.HeaderMenu-link--sign-in")

    @allure.step("Перейти на главную страницу")
    def open_main_page(self):
        self.driver.get(self._URL)

    @allure.step("Нажать на кнопку Sign In")
    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self._SIGN_IN_BTN)).click()

    def go_to_login(self):
        self.open_main_page()
        self.click_sign_in()
