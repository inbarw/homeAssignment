from selenium.webdriver.common.by import By
from pages.base_page import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.ID, 'loginEmail')
        self.password_field = (By.ID, 'loginPassword')
        self.login_button = (By.CSS_SELECTOR, 'button[type=submit]')
        self.firm_dropdown = (By.CSS_SELECTOR,'select#orgId')

    def fill_email(self, email):
        self.find_element(*self.email_field).send_keys(email)

    def fill_password(self, password):
        self.find_element(*self.password_field).send_keys(password)

    def login(self, email: str, password: str, firm_option: str):
        self.wait_for_element_to_be_visible(self.email_field)
        self.fill_email(email)
        self.fill_password(password)
        self.find_element(*self.login_button).click()
        self.wait_for_element_to_be_visible(self.firm_dropdown)
        self.select_dropdown_option_by_text(*self.firm_dropdown, firm_option)
        self.find_element(*self.login_button).click()





