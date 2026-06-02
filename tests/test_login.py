import allure

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Login")
def test_successful_login(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "secret_sauce")
    assert InventoryPage(browser).is_opened()


@allure.feature("Login")
def test_invalid_password_error(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "wrong_password")
    assert "Username and password do not match" in login.error_text()


@allure.feature("Login")
def test_locked_out_user_error(browser):
    login = LoginPage(browser).open_login()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error_text()

