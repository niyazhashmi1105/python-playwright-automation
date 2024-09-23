from playwright.sync_api import Page
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage



class LoginPage(BasePage):

    URL ='/'

    def __init__(self, page:Page) -> None:
        super().__init__(page)
        self.username_input = LoginPageLocators.USERNAME_TXT_BOX
        self.password_input = LoginPageLocators.PASSWORD_TXT_BOX
        self.login_btn = LoginPageLocators.LOGIN_BTN
        self.title = LoginPageLocators.PAGE_TITLE
        self.log_in_error_text = LoginPageLocators.LOGIN_ERROR_TEXT

    def do_login(self,username: str, password: str) -> None:
        self.input_text(self.username_input,username)
        self.input_text(self.password_input, password)
        self.click_element(self.login_btn)

    def get_page_title_text(self):
       return self.get_page_title(self.title)

    def validate_login_error_is_visible(self):
        return self.is_element_visible(self.log_in_error_text)




