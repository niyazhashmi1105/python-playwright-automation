import pytest
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.login_page import LoginPage

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
def login_page(page:Page):
    return LoginPage(page)

