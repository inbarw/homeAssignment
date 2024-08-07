from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Base


class ClientsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_new_client_button = (By.ID, 'addNewClientBtnId')
        self.first_name_field = (By.ID, 'first_name')
        self.last_name_field = (By.ID, 'last_name')
        self.ssn_field = (By.ID, 'ssn')
        self.email_field = (By.ID, 'email')
        self.mobile_field = (By.ID, 'contactPhone')
        self.city_field = (By.ID, 'city')
        self.state_dropdown = (By.CSS_SELECTOR, 'button[title="Select state"]')
        self.state_text_field = (By.CSS_SELECTOR, 'input[aria-controls="bs-select-1"]')
        self.advisor_dropdown = (By.CSS_SELECTOR, 'button[title="Select Advisor"]')
        self.advisor_text_field = (By.CSS_SELECTOR, 'input[aria-controls="bs-select-2"]')
        self.add_client_button = (By.ID, 'save-client-changes-btn')
        self.clients_link_breadcrumbs = (By.CSS_SELECTOR, 'a[href="/qaa/advisor/clients"]')
        self.client_name_in_grid = (By.XPATH, '//span[text()="NAME"]/ancestor::table/descendant::a[text()="CLIENT_NAME"]')

    def fill_first_name(self, first_name: str):
        self.find_element(*self.first_name_field).send_keys(first_name)

    def fill_last_name(self, last_name: str):
        self.find_element(*self.last_name_field).send_keys(last_name)

    def fill_ssn(self, ssn: str):
        self.find_element(*self.ssn_field).send_keys(ssn)

    def fill_email(self, email: str):
        self.find_element(*self.email_field).send_keys(email)

    def fill_mobile(self, mobile: str):
        self.find_element(*self.mobile_field).send_keys(mobile)

    def fill_city(self, city: str):
        self.find_element(*self.city_field).send_keys(city)

    def fill_state(self, state: str):
        self.find_element(*self.state_dropdown).click()
        self.find_element(*self.state_text_field).send_keys(state + Keys.ENTER)

    def fill_advisor(self, advisor: str):
        self.find_element(*self.advisor_dropdown).click()
        self.find_element(*self.advisor_text_field).send_keys(advisor + Keys.ENTER)


    def add_new_client(self, first_name: str, last_name: str, ssn: str, email: str, mobile_phone:str,
                       city: str, state: str, advisor_name: str):
        self.wait_for_element_to_be_visible(self.add_new_client_button)
        self.wait_for_element_to_be_clickable_and_click(self.add_new_client_button)
        self.wait_for_element_to_be_visible(self.first_name_field)
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_ssn(ssn)
        self.fill_email(email)
        self.fill_mobile(mobile_phone)
        self.fill_city(city)
        self.fill_state(state)
        self.fill_advisor(advisor_name)
        self.find_element(*self.add_client_button).click()

    def verify_client_name_in_grid(self, client_name):
        client_name_locator = (self.client_name_in_grid[0], self.client_name_in_grid[1].replace("CLIENT_NAME", client_name))
        try:
            self.wait_for_element_to_be_visible(client_name_locator)
            return self.find_element(*client_name_locator)
        except TimeoutException:
            print(f"The client name '{client_name}' was not visible within the timeout period.")
            return None


    def navigate_to_clients_tab_from_client_details(self):
        self.wait_for_element_to_be_visible(self.clients_link_breadcrumbs)
        self.find_element(*self.clients_link_breadcrumbs).click()


    def delete_client(self):
        return







