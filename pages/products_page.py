from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.products_page_locators import ProductsPageLocators
from playwright.sync_api import Page


class ProductsPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.product_header = ProductsPageLocators.PRODUCT_HEADER
        self.hamburger_menu = ProductsPageLocators.HAMBURGER_MENU
        self.logout_btn = ProductsPageLocators.LOGOUT_BTN

    @property
    def get_product_header_text(self):
        return self.get_text(self.product_header)

    def click_hamburger_menu(self):
        self.click_element(self.hamburger_menu)

    def click_logout(self):
        self.click_element(self.logout_btn)