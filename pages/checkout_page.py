from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    TITLE = (By.XPATH, "//span[@data-test='title' and text()='Checkout: Your Information']")
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE = (By.CSS_SELECTOR, "[data-test='continue']")
    ERROR = (By.XPATH, "//h3[@data-test='error']")
    FINISH = (By.CSS_SELECTOR, "[data-test='finish']")
    COMPLETE_TITLE = (By.XPATH, "//span[@data-test='title' and text()='Checkout: Complete!']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def is_opened(self):
        return self.is_visible(self.TITLE)

    def continue_checkout(self):
        self.click(self.CONTINUE)

    def fill_customer(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    def error_text(self):
        return self.text_of(self.ERROR)

    def finish_order(self):
        self.click(self.FINISH)

    def complete_text(self):
        self.find_visible(self.COMPLETE_TITLE)
        return self.text_of(self.COMPLETE_HEADER)
