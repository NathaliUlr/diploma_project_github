# diploma_project_github

## Дипломная работа. Тестирование платформы GitHub
Данный проект представляет собой тестовый фреймворк для проверки функциональности GitHub
(создание, удаление, редактирование репозиториев) через **UI** (Selenium) и **API** (Requests).

### Шаги
1. Склонировать проект 'git clone https://github.com/NathaliUlr/diploma_project_github.git'
2. Установка всех необходимых зависимостей pip3 install > -r requirements.txt
3. Конфигурация:
   Убедиться, что в файле config.py указаны актуальные данные:
   USERNAME и GITHUB_TOKEN (для API тестов)
   Логин/Пароль (для авторизации в UI тестах)
   Внести свои данные в USERNAME, PASSWORD, GITHUB_TOKEN
4. Запуск тестов и сбор данных для отчета
   Запуск по категориям (маркерам): 
   Только UI тесты: pytest -m ui --alluredir=allure-results
   Только API тесты: pytest -m api --alluredir=allure-results
5. Работа с отчетами Allure.
   После завершения тестов, после появлени папки allure-results, сгенерировать HTML-отчет:
   allure generate allure-results -o allure-report --clean
6. Просмотр отчета.
   Чтобы открыть сформированный отчет в браузере: allure open allure-report

### Стек технологий:
Язык: Python
Тестовый фреймворк: Pytest
UI тесты: Selenium WebDriver
API тесты: Requests
Отчетность: Allure Framework
Логика страниц: Page Object Model

### Структура:
api/  — вспомогательные классы и методы для работы с GitHub API.
pages/ — описание страниц (Page Objects) для UI тестов.
test/ — директория с тестами (разделена на `ui` и `api`).
config.py — конфигурационный файл (токены, URL, тестовые данные).
conftest.py — настройки pytest, фикстуры для инициализации браузера и API-клиентов.
pytest.ini — регистрация маркеров и базовые настройки запуска.

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Документация Pytest](https://docs.pytest.org/)
- [Allure Framework Guide](https://docs.qameta.io/allure/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

### Ссылка на финальный проект по ручному тестированию
- [финальный проект](https://ulrikhns-qa121-2-skypro.yonote.ru/share/f1aa7ffc-a9b8-4b69-a104-522eeeb40fa7)