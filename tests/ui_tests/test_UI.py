from pages.clients_page import ClientsPage
from pages.login_page import LoginPage
from utils.client_data_utils import set_client_data


def test_UI(browser):
    url = 'https://advisor-test.pontera.com/business/auth/signin.html'
    login_email = 'Maayan+Tester1@feex.com'
    login_password = 'Advisor0103Buckley'
    login_firm = 'QA Advisors'

    login_page = LoginPage(browser)
    login_page.navigate(url)
    login_page.login(login_email, login_password, login_firm)

    clients_page = ClientsPage(browser)
    client_data = set_client_data('Test', 'User', '123456789', 'test@gmail.com', '0542222222', 'Tel Aviv', 'Alabama', 'Maayan Tester1')
    clients_page.add_new_client(client_data)
    clients_page.navigate_to_clients_tab_from_client_details()
    is_client_name_in_grid = clients_page.verify_client_name_in_grid(client_data['first_name'] + " " + client_data['last_name'])
    assert is_client_name_in_grid is not None


