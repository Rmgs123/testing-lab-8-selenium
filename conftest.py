import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def browser():
    options = Options()
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.binary_location = os.getenv("CHROME_BINARY", "/usr/bin/chromium-browser")
    driver_path = os.getenv("CHROMEDRIVER")
    if driver_path:
        driver = webdriver.Chrome(service=Service(driver_path), options=options)
    else:
        driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, browser):
    yield
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        allure.attach(browser.get_screenshot_as_png(), name="failure", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
