import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from config import GITHUB_URL


class DeletePage(BasePage):
    DELETE_BUTTON_START = (By.XPATH, '//span[text()="Delete this repository"]')
    CONFIRM_PROCEED_1 = (
        By.XPATH, '//span[text()="I want to delete this repository"]')
    CONFIRM_PROCEED_2 = (
        By.XPATH, '//span[text()="I have read and understand these effects"]')
    VERIFICATION_FIELD = (By.ID, 'verification_field')
    FINAL_DELETE_BUTTON = (By.ID, 'repo-delete-proceed-button')

    @allure.step("Полное удаление репозитория: {repo_full_name}")
    def delete_repository(self, repo_full_name):
        with allure.step(f"Переход в настройки: {repo_full_name}"):
            self.driver.get(f"{GITHUB_URL}/{repo_full_name}/settings")

        with allure.step("Инициировать удаление"):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            self.wait.until(
                EC.element_to_be_clickable(self.DELETE_BUTTON_START)).click()

        with allure.step("Подтверждение этапов"):
            self.wait.until(EC.element_to_be_clickable(
                self.CONFIRM_PROCEED_1)).click()
            self.wait.until(EC.element_to_be_clickable(
                self.CONFIRM_PROCEED_2)).click()

        with allure.step(f"Ввод имени '{repo_full_name}'"):
            field = self.wait.until(
                EC.visibility_of_element_located(self.VERIFICATION_FIELD))
            field.clear()
            for char in repo_full_name:
                field.send_keys(char)

        with allure.step("Нажатие финальной кнопки удаления"):
            final_btn = self.wait.until(
                EC.element_to_be_clickable(self.FINAL_DELETE_BUTTON)
            )
            final_btn.click()

        with allure.step("Проверка после удаления"):
            self.wait.until_not(
                EC.url_contains("/settings"),
                message=f"Ошибка: Репозиторий {repo_full_name} не был удален"
            )
