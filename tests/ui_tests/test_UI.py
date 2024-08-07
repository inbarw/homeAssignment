from pages.clients_page import ClientsPage
from pages.login_page import LoginPage


def test_UI(browser):
    url = 'https://advisor-test.pontera.com/business/auth/signin.html'
    login_email = 'Maayan+Tester1@feex.com'
    login_password = 'Advisor0103Buckley'
    login_firm = 'QA Advisors'
    client_first_name = 'Test'
    client_last_name = 'User'
    client_ssn = '123456789'
    client_email = 'test@gmail.com'
    client_mobile = '0542222222'
    client_city = 'Tel Aviv'
    client_state = 'Alabama'
    client_advisor_name = 'Maayan Tester1'

    login_page = LoginPage(browser)
    login_page.navigate(url)
    login_page.login(login_email, login_password, login_firm)

    clients_page = ClientsPage(browser)
    clients_page.add_new_client(client_first_name, client_last_name, client_ssn, client_email, client_mobile,
                                client_city, client_state, client_advisor_name)
    clients_page.navigate_to_clients_tab_from_client_details()
    is_client_name_in_grid = clients_page.verify_client_name_in_grid(client_first_name + " " + client_last_name)
    assert is_client_name_in_grid is not None


