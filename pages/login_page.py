from playwright.sync_api import Page
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.products_page import ProductsPage


class LoginPage(BasePage):


    def __init__(self, page:Page) -> None:
        super().__init__(page)
        self.username_input = LoginPageLocators.USERNAME_TXT_BOX
        self.password_input = LoginPageLocators.PASSWORD_TXT_BOX
        self.login_btn = LoginPageLocators.LOGIN_BTN
        self.title = LoginPageLocators.PAGE_TITLE
        self.log_in_error_text = LoginPageLocators.LOGIN_ERROR_TEXT

    def do_login(self,username: str, password: str) -> ProductsPage:
        self.input_text(self.username_input,username)
        self.input_text(self.password_input, password)
        self.click_element(self.login_btn)
        return ProductsPage(self.page)

    def get_page_title_text(self):
       return self.get_page_title(self.title)

    def is_login_error_visible(self):
        return self.is_element_visible(self.log_in_error_text)

    def is_login_btn_visible(self):
        return self.is_element_visible(self.login_btn)




