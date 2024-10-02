import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
        # 'viewport':{
        #         'width':  1280,
        #         'height': 1024,
        # },
    }


@pytest.fixture()
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture()
def products_page(page: Page):
    return ProductsPage(page)
