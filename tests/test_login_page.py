from pages.login_page import LoginPage


def test_login_page_with_valid_credentials(login_page: LoginPage) -> None:
    login_page.go_to_url()
    login_page.do_login('standard_user', 'secret_sauce')
    assert login_page.get_page_title_text() == 'Swag Labs', "page title not correct,Assertion failed!!"


def test_login_page_locked_user_error(login_page: LoginPage) -> None:
    login_page.go_to_url()
    login_page.do_login('locked_out_user', 'secret_sauce')
    assert login_page.is_login_error_visible() == True, "Error Message is visible"
