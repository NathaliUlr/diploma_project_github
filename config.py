"""
Конфигурационные данные для тестов
"""

# Данные для авторизации
USERNAME = ""  # внести свои данные
PASSWORD = ""  # внести свои данные

# URL GitHub
GITHUB_URL = "https://github.com"
GITHUB_LOGIN_URL = "https://github.com/login"
GITHUB_NEW_REPO_URL = "https://github.com/new"

# Данные для API
GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = ""  # внести свои данные

# Названия репозиториев для API тестов
API_REPO_NAME_1 = "PROJECT"
# Имя в верхнем регистре (тест с неверным токен)
API_REPO_NAME_2 = "lesson"  # латинские символы
API_REPO_NAME_3 = "S"  # Односимвольное имя
API_REPO_NAME_4 = "ui"  # Двухсимвольное имя
API_REPO_NAME_5 = "1234567890"  # Числовое имя
API_REPO_NAME_6 = "Documentation"  # Имя в верхнем и нижнем регистре
API_REPO_NAME_7 = "iplayoutsideiliketoplayireadabookiliketoreadbooksi"
# 50 символов в имени
API_REPO_NAME_8 = (
    "foralmostanpersonthereisnothingmoreimportantintheworld"
    "thantheirfamilyovemyfamilytooforalmostanpfora"
)
# 99 символов в имени
API_REPO_NAME_9 = (
    "foralmostanpersonthereisnothingmoreimportantintheworld"
    "thantheirfamilyovemyfamilytooforalmostanpforad"
)
# 100 символов в имени
API_REPO_NAME_10 = "lesson"
# латинские символы (тест на добавление описания)
API_REPO_NAME_11 = "Дипломный проект"  # Имя на кириллице
API_REPO_NAME_12 = "冬天有很多节日"  # Иероглифы

# Описание репозитория для API тестов
API_REPO_DESCRIPTION_1 = "This is a test description"

# Названия репозиториев для UI тестов
UI_REPO_NAME_1 = "r"  # Односимвольное имя
UI_REPO_NAME_2 = "ns"  # Двухсимвольное имя
UI_REPO_NAME_3 = "iplayoutaidealikatopaayiaeadaaookiaikeaoreadbaoasi"
# 50 символов в имени
UI_REPO_NAME_4 = "89826071198"  # Числовое имя
UI_REPO_NAME_5 = "NaTaLyA"  # Имя в верхнем и нижнем регистре
UI_REPO_NAME_6 = "PLAN"  # Имя в верхнем регистре

# Полные пути репозиториев для удаления
FULL_UI_REPO_1 = f"{USERNAME}/{UI_REPO_NAME_1}"
FULL_UI_REPO_2 = f"{USERNAME}/{UI_REPO_NAME_2}"
FULL_UI_REPO_3 = f"{USERNAME}/{UI_REPO_NAME_3}"
FULL_UI_REPO_4 = f"{USERNAME}/{UI_REPO_NAME_4}"
FULL_UI_REPO_5 = f"{USERNAME}/{UI_REPO_NAME_5}"
FULL_UI_REPO_6 = f"{USERNAME}/{UI_REPO_NAME_6}"

# Таймауты
IMPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30
