# Sprint_6 — автотесты для сервиса «Яндекс.Самокат»

Финальный проект 6 спринта. UI-автотесты на Python + Selenium + pytest + Allure 
с использованием паттерна Page Object Model.

## Что проверяется

1. **FAQ «Вопросы о важном»** — 8 вопросов аккордеона, при клике на каждый 
   открывается соответствующий текст.
2. **Заказ самоката** — позитивный флоу с двумя наборами данных и с двух точек 
   входа (верхняя и нижняя кнопки «Заказать»).
3. **Навигация по логотипам** — клик по логотипу «Самоката» ведёт на главную, 
   клик по логотипу «Яндекса» открывает Дзен в новой вкладке.

## Стек

- Python 3.9+
- Selenium 4.x
- pytest
- allure-pytest
- Firefox + geckodriver

## Структура проекта

```
Sprint_6/
├── data/                       # тестовые данные
│   ├── urls.py                 # адреса сервиса
│   ├── order_data.py           # наборы данных для заказа
│   └── faq_data.py             # вопросы и ответы FAQ
├── locators/                   # локаторы элементов
│   ├── main_page_locators.py   # главная страница
│   └── order_page_locators.py  # страница заказа
├── pages/                      # Page Object Model
│   ├── base_page.py            # базовые методы для всех страниц
│   ├── main_page.py            # главная страница
│   └── order_page.py           # страница оформления заказа
├── tests/                      # тесты
│   ├── test_faq.py             # 8 тестов на FAQ
│   ├── test_order.py           # 4 теста на заказ (2 набора × 2 кнопки)
│   └── test_navigation.py      # 2 теста на логотипы
├── allure-report/              # сгенерированный HTML-отчёт
├── conftest.py                 # фикстура driver
├── pytest.ini                  # настройки pytest
├── requirements.txt            # зависимости
└── README.md
```

## Установка

```bash
# Клонировать репозиторий
git clone git@github.com:<username>/Sprint_6.git
cd Sprint_6

# Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt
```

**Требования к окружению:**
- Установленный Firefox
- `geckodriver` в PATH (проверка: `geckodriver --version`)
- Allure Commandline (для генерации отчёта)

## Запуск тестов

**Все тесты:**
```bash
pytest
```

**Отдельный файл:**
```bash
pytest tests/test_order.py -v
```

**Отдельный тест:**
```bash
pytest tests/test_faq.py::TestFaq::test_faq_answer -v
```

## Allure-отчёт

**Прогнать тесты с сохранением результатов:**
```bash
pytest --alluredir=allure-results
```

**Сгенерировать HTML-отчёт:**
```bash
allure generate allure-results -o allure-report --clean
```

**Посмотреть отчёт:**
```bash
allure open allure-report
```

Готовый отчёт уже лежит в папке `allure-report/` — можно открыть 
файл `allure-report/index.html` в браузере.

## Архитектура

Проект построен на паттерне **Page Object Model**:

- **Page Object** — отдельный класс на каждую страницу сайта. Внутри класса — 
  локаторы и методы для взаимодействия со страницей.
- **BasePage** — родительский класс с общими методами (`open`, `click`, 
  `send_keys`, `get_text`, ожидания). Все Page Object наследуются от него.
- **Тесты** не обращаются к `driver` напрямую — только вызывают методы пейджей.
- **Локаторы** вынесены в отдельную папку `locators/` и хранятся списками 
  `[By.XPATH, "..."]`.
- **Тестовые данные** вынесены в папку `data/`.