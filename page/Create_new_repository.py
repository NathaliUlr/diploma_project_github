import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CreateNewRepository(BasePage):
    _NAME_INPUT = (By.ID, "repository-name-input")
    _BTN = (By.XPATH, "//button[contains(., 'Create repository')]")
    _VALID = (By.ID, "RepoNameInput-is-available")

    @allure.step("Создать репозиторий: {name}")
    def create_repo(self, name: str):

        with allure.step(f"Ввести имя репозитория: {name}"):
            self.wait.until(
                EC.visibility_of_element_located(
                    self._NAME_INPUT)).send_keys(name)

        with allure.step("Дождаться проверки доступности имени и кликнуть"):
            self.wait.until(EC.visibility_of_element_located(self._VALID))
            btn = self.wait.until(EC.element_to_be_clickable(self._BTN))

            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", btn)

            btn.click()

        with allure.step("Проверить переход в созданный репозиторий"):
            self.wait.until(EC.url_contains(name))
