# testing-lab-8-selenium

UI-автотесты на Selenium для сайта Saucedemo.

## Стек

- Python
- pytest
- Selenium WebDriver
- Selenium Manager
- Allure
- Page Object
- Explicit Wait
- CSS- и XPath-локаторы

## Покрытые тест-кейсы

1. Успешный вход в систему.
2. Ошибка при вводе неверного пароля.
3. Ошибка при входе заблокированного пользователя.
4. Отображение списка товаров после входа.
5. Сортировка товаров по цене от меньшей к большей.
6. Добавление товара в корзину.
7. Удаление товара из корзины.
8. Переход к оформлению заказа из корзины.
9. Ошибка при пустых обязательных полях оформления заказа.
10. Успешное оформление заказа.

## Запуск на Windows

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Запуск на Linux или macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Allure-отчёт

Сначала нужно запустить тесты с генерацией результатов:

```bash
pytest --alluredir=allure-results
```

Затем открыть отчёт:

```bash
allure serve allure-results
```

## Режим браузера

По умолчанию тесты запускаются в headless-режиме, то есть без видимого окна браузера.

Чтобы запустить тесты с обычным окном браузера:

```bash
HEADLESS=0 pytest
```

В PowerShell на Windows можно выполнить так:

```powershell
$env:HEADLESS="0"
pytest
```
