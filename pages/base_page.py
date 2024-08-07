

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Base():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def select_dropdown_option_by_text(self, by: By, value, option: str):
        dropdown_element = self.find_element(by, value)
        select = Select(dropdown_element)
        select.select_by_visible_text(option)

    def wait_for_element_to_be_clickable_and_click(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(locator)).click()

    def find_elements(self, by: By, value: str):
        return self.driver.find_elements(by, value)


