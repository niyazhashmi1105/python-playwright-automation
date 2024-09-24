import threading
from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


class Tls(threading.local):
    def __init__(self) -> None:
        self.playwright = sync_playwright().start()
        print("Create playwright instance in Thread", threading.current_thread().name)


class Worker:
    tls = Tls()

    def run(self):
        print("Launched worker in ", threading.current_thread().name)
        browser = self.tls.playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        page.goto("http://whatsmyuseragent.org/")
        page.screenshot(path=f"example-{threading.current_thread().name}.png")
        page.close()
        context.close()
        browser.close()
        print("Stopped worker in ", threading.current_thread().name)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(10):
            worker = Worker()
            executor.submit(worker.run)