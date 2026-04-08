import pytest
import config
import allure


@allure.epic("GitHub API")
@allure.feature("Операции с репозиториями")
@pytest.mark.api
class TestGitHubAPI:
    @allure.title("Получение списка репозиториев пользователя")
    @allure.description(
        "Проверка получения списка всех публичных репозиториев пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_repo(self, repo_api):
        with allure.step(f"Список репозиториев для {config.USERNAME}"):
            repo_list = repo_api.get_user_repositories(config.USERNAME).json()
        with allure.step("Проверка, что вернулся список"):
            assert isinstance(repo_list, list)

    @allure.title("Создание репозитория: неверный токен (негативный)")
    @allure.description(
        "Проверка отказа в доступе при использовании некорректного токена")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_invalid_token(self, bad_repo_api):
        name = config.API_REPO_NAME_1
        with allure.step("Попытка создания репозитория с неверным токеном"):
            resp = bad_repo_api.create_repository(name)
        with allure.step("Проверка на статус-код 401 Unauthorized"):
            assert resp.status_code == 401

    @allure.title("Создание репозитория: пустое имя (негативный)")
    @allure.description(
        "Проверка ошибки при попытке создать репозиторий без названия")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_repo_empty_name(self, repo_api):
        name = ""
        with allure.step("Попытка создания репозитория с пустым именем"):
            resp = repo_api.create_repository(name)
        with allure.step("Проверка статус-кода ошибки (422)"):
            assert resp.status_code == 422
        with allure.step("Проверка сообщения об ошибке"):
            error_data = resp.json()
            assert "errors" in error_data
            assert error_data["message"] == (
                "New repository name must not be blank")

    @allure.title("Создание репозитория: имя из латинских символов")
    @allure.description(
        "Проверка корректности создания репозитория, "
        "чье имя состоит только из латинских символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_latin_symbols(self, repo_manager):
        name = config.API_REPO_NAME_2
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Удаление репозитория: минимальная длина названия")
    @allure.description(
        "Проверка процесса удаления репозитория с названием из 1 символа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_repo_minimal_length_repo(self, repo_api, repo_manager):
        name = config.API_REPO_NAME_3
        with allure.step(f"Подготовка: Создать репозиторий '{name}'"):
            create_resp = repo_manager(name)
            assert create_resp.status_code == 201, "Репозиторий не был создан"
        import time
        time.sleep(1)
        with allure.step(f"Удалить репозиторий '{name}'"):
            delete_resp = repo_api.delete_repository(name)
        with allure.step("Проверка успешного удаления (204)"):
            assert delete_resp.status_code == 204

    @allure.title("Создание репозитория: имя из двух символов")
    @allure.description(
        "Проверка корректности создания репозитория, "
        "чье имя состоит из двух символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_two_symbols(self, repo_manager):
        name = config.API_REPO_NAME_4
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Создание репозитория: имя состоящее из цифр")
    @allure.description(
        "Проверка корректности создания репозитория, "
        "чье имя состоит из цифр")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_numeric_only(self, repo_manager):
        name = config.API_REPO_NAME_5
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Создание репозитория: смешанный регистр символов")
    @allure.description("Проверка создания репозитория, когда имя содержит "
                        "заглавные и строчные буквы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_mixed_register(self, repo_manager):
        name = config.API_REPO_NAME_6
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Создание репозитория: 50 символов в имени")
    @allure.description(
        "Проверка создания репозитория с длиной названия в 50 символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_50_symbols(self, repo_manager):
        name = config.API_REPO_NAME_7
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Создание репозитория: 99 символов в имени")
    @allure.description(
        "Проверка создания репозитория с длиной названия в 50 символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_99_symbols(self, repo_manager):
        name = config.API_REPO_NAME_8
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Создание репозитория: 100 символов в имени")
    @allure.description(
        "Проверка создания репозитория с длиной названия в 50 символов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_repo_100_symbols(self, repo_manager):
        name = config.API_REPO_NAME_9
        with allure.step(f"Создать репозиторий '{name}'"):
            resp = repo_manager(name)
            assert resp.status_code == 201

    @allure.title("Изменение описания (PATCH)")
    @allure.description(
        "Проверка обновления поля description существующего репозитория")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_repo_description(self, repo_api, repo_manager):
        name_from_config = config.API_REPO_NAME_10
        new_description = config.API_REPO_DESCRIPTION_1
        with allure.step(
             f"Подготовка: Создать репозиторий '{name_from_config}'"):
            create_res = repo_manager(name_from_config)
            assert create_res.status_code == 201
            real_name = create_res.json().get("name")
        with allure.step("Ожидание синхронизации базы данных GitHub"):
            import time
            time.sleep(1)
        with allure.step(
             f"Отправить PATCH запрос на изменение описания '{real_name}'"):
            edit_res = repo_api.edit_repository(real_name, new_description)
        with allure.step("Проверка: статус 200 и новое описание в ответе"):
            assert edit_res.status_code == 200
            assert edit_res.json().get("description") == new_description

    @allure.title("Создание репозитория: в имени символы кириллицы")
    @allure.description("Попытка создать репозиторий с названием на кириллице,"
                        "GitHub автоматически заменяет имя на дефис '-'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_repo_cyrillic(self, repo_api):
        name_with_cyrillic = config.API_REPO_NAME_11
        target_name = "-"
        with allure.step(f"Удалить старый '{target_name}', если он есть"):
            repo_api.delete_repository(target_name)
        with allure.step(
             f"Создать репозиторий с кириллицей '{name_with_cyrillic}'"):
            resp = repo_api.create_repository(name_with_cyrillic)
        assert resp.status_code == 201
        res_json = resp.json()
        real_name = res_json.get("name")
        try:
            with allure.step(f"Проверка: имя заменено на '{target_name}'"):
                assert real_name == target_name
        finally:
            with allure.step(
                 f"Cleanup: Удаление созданного репозитория '{target_name}'"):
                repo_api.delete_repository(target_name)

    @allure.title("Создание репозитория: в имени символы иероглифы")
    @allure.description("Попытка создать репозиторий с именем,"
                        "в котором используются иероглифы,"
                        "GitHub автоматически заменяет имя на дефис '-'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_repo_hieroglyphs(self, repo_api):
        name_with_hieroglyphs = config.API_REPO_NAME_12
        target_name = "-"
        with allure.step(f"Удалить старый '{target_name}', если он есть"):
            repo_api.delete_repository(target_name)
        with allure.step(
             f"Создать репозиторий с иероглифами '{name_with_hieroglyphs}'"):
            resp = repo_api.create_repository(name_with_hieroglyphs)
        assert resp.status_code == 201
        res_json = resp.json()
        real_name = res_json.get("name")
        try:
            with allure.step(f"Проверка: имя заменено на '{target_name}'"):
                assert real_name == target_name
        finally:
            with allure.step(
                 f"Cleanup: Удаление созданного репозитория '{target_name}'"):
                repo_api.delete_repository(target_name)
