import allure

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


PRODUCT = "Sauce Labs Backpack"


@allure.feature("Cart")
def test_add_product_to_cart(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser)
    inventory.add_item(PRODUCT)
    assert inventory.cart_count() == "1"
    inventory.open_cart()
    assert CartPage(browser).has_item(PRODUCT)


@allure.feature("Cart")
def test_remove_product_from_cart(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser)
    inventory.add_item(PRODUCT)
    inventory.open_cart()
    cart = CartPage(browser)
    cart.remove_item(PRODUCT)
    assert cart.item_count() == 0
