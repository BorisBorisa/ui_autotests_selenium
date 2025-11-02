# UI Automation Selenium Tests

Этот проект реализует автоматизированные тесты для [DemoQA](https://demoqa.com/).

## Описание

Этот проект представляет собой фреймворк для автоматизации UI-тестирования веб-приложений на базе Selenium.
В качестве демонстрационной площадки используется сайт DemoQA.

Проект разработан в рамках практики написания UI-автотестов и включает:
- Page Object Model (POM) для структурирования тестов
- Реализация Singleton WebDriver
- Гибкая конфигурация окружения через Pydantic
- Подробные Allure-отчёты с шагами, и логами
- Управление тестовыми данными и окружением через конфигурационные файлы
- Поддержка кросс-браузерного тестирования (Chrome, Firefox, Edge)

## Технологии

- **Python** - основной язык программирования
- **Selenium** - автоматизация UI-тестирования веб-приложений
- **Pytest** - фреймворк для написания и запуска тестов
- **Allure** - генерация детализированных отчётов о тестах
- **Pydantic** - управление настройками и загрузка тестовых данных

### Allure отчет

Результаты выполнения тестов доступны по ссылке: [Allure report]().

## Начало работы

### Клонирование репозитория

```
git clone https://github.com/BorisBorisa/ui_autotests_playwright.git
cd api_autotests
```

### Создание виртуального окружения
#### Linux / MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Запуск тестов с генерацией отчета Allure
```bash
pytest -m "regression" --alluredir=./allure-results
```
Эта команда запустит все тесты проекта и выведет результаты в терминале.

### Просмотр отчета Allure
```bash
allure serve allure-results
```
Эта команда откроет отчет Allure в браузере по умолчанию.