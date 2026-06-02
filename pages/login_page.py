from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")
    ERROR = (By.XPATH, "//h3[@data-test='error']")

    def open_login(self):
        self.open(self.URL)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_text(self):
        return self.text_of(self.ERROR)
