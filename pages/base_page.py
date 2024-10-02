
from playwright.sync_api import Page
import os

class BasePage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page) -> None:
        self.page = page


    def go_to_url(self) -> None:
        self.page.goto(self.URL)

    def input_text(self, locator: str, text: str):
        self.page.locator(locator).clear()
        self.page.locator(locator).fill(text)

    def click_element(self,locator):
        self.page.click(locator)

    def get_page_title(self,locator):
       return self.page.inner_text(locator)

    def is_element_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str):
        self.page.locator(locator).wait_for()

    def click_and_wait_for_navigation(self, locator: str):
        with self.page.expect_navigation():
            self.page.locator(locator).click()

    def get_text(self,locator):
        return self.page.inner_html(locator)

    def take_screenshot(self, name: str):
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.page.screenshot(path=screenshot_path)

