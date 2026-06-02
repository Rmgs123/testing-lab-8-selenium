import allure

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Inventory")
def test_inventory_list_is_displayed_after_login(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser)
    assert inventory.is_opened()
    assert inventory.item_count() == 6


@allure.feature("Inventory")
def test_sort_products_by_price_low_to_high(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser)
    inventory.sort_by_value("lohi")
    prices = inventory.prices()
    assert prices == sorted(prices)
