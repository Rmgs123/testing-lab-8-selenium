from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.XPATH, "//span[@data-test='title' and text()='Products']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT_LINK = (By.XPATH, "//a[@data-test='logout-sidebar-link']")

    def is_opened(self):
        return self.is_visible(self.TITLE)

    def item_count(self):
        return len(self.find_all_visible(self.ITEMS))

    def add_item(self, item_name):
        self.click((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{item_name}']/ancestor::div[@data-test='inventory-item']//button"))

    def remove_item(self, item_name):
        self.click((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{item_name}']/ancestor::div[@data-test='inventory-item']//button"))

    def cart_count(self):
        return self.text_of(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_by_value(self, value):
        select = self.find_visible(self.SORT_SELECT)
        select.click()
        self.click((By.CSS_SELECTOR, f"option[value='{value}']"))

    def prices(self):
        values = []
        for element in self.find_all_visible(self.PRICES):
            values.append(float(element.text.replace("$", "")))
        return values

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
