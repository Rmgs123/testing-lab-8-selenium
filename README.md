# testing-lab-8-selenium

Selenium UI autotests for Saucedemo.

## Stack

- Python
- pytest
- Selenium WebDriver
- Selenium Manager
- Allure
- Page Object
- Explicit Wait
- CSS and XPath locators

## Test cases

1. Successful login.
2. Invalid password error.
3. Locked-out user error.
4. Inventory list is displayed after login.
5. Product sorting by price from low to high.
6. Add product to cart.
7. Remove product from cart.
8. Open checkout from cart.
9. Checkout required fields error.
10. Successful checkout.

## Run on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Run on Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Allure

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Browser mode

Headless mode is enabled by default.

```bash
HEADLESS=0 pytest
```
