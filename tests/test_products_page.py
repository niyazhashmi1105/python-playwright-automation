from pages.products_page import ProductsPage
from pages.login_page import LoginPage


def test_product_header_text(login_page: LoginPage, products_page: ProductsPage):
    login_page.go_to_url()
    products_page = login_page.do_login('standard_user', 'secret_sauce')
    product_header = products_page.get_product_header_text
    assert product_header == 'Products',"Products Header Text failed to display"

def test_logout(login_page: LoginPage, products_page: ProductsPage):
    login_page.go_to_url()
    login_page.do_login('standard_user', 'secret_sauce')
    products_page.click_hamburger_menu()
    products_page.click_logout()
    assert login_page.is_login_btn_visible() == True,"Login button not visible,Assertion failed!!"