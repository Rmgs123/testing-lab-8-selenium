import allure

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


PRODUCT = "Sauce Labs Backpack"


def open_checkout(browser):
    login = LoginPage(browser).open_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser)
    inventory.add_item(PRODUCT)
    inventory.open_cart()
    cart = CartPage(browser)
    cart.checkout()
    return CheckoutPage(browser)


@allure.feature("Checkout")
def test_open_checkout_from_cart(browser):
    checkout = open_checkout(browser)
    assert checkout.is_opened()


@allure.feature("Checkout")
def test_checkout_required_fields_error(browser):
    checkout = open_checkout(browser)
    checkout.continue_checkout()
    assert "First Name is required" in checkout.error_text()


@allure.feature("Checkout")
def test_successful_checkout(browser):
    checkout = open_checkout(browser)
    checkout.fill_customer("Roman", "Popovichenko", "690000")
    checkout.finish_order()
    assert checkout.complete_text() == "Thank you for your order!"
