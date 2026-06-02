from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.XPATH, "//span[@data-test='title' and text()='Your Cart']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")

    def is_opened(self):
        return self.is_visible(self.TITLE)

    def has_item(self, item_name):
        return self.is_visible((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{item_name}']"))

    def remove_item(self, item_name):
        self.click((By.XPATH, f"//div[@data-test='inventory-item-name' and text()='{item_name}']/ancestor::div[@data-test='inventory-item']//button"))

    def item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
