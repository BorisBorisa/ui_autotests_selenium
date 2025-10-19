from tools.webdriver.singleton import Singleton

from selenium.webdriver.chrome.webdriver import WebDriver

from tools.webdriver.browser import get_browser_driver
from config import Browser


class DriverManger(metaclass=Singleton):
    def __init__(self, ):
        self._driver: WebDriver | None = None

    def init(self, browser: Browser):
        self._driver = get_browser_driver(browser)

    @property
    def driver(self) -> WebDriver:
        if self._driver is None:
            raise RuntimeError("Driver not initialized. Call init(browser) first.")
        return self._driver

    def close_driver(self):
        if self._driver:
            self._driver.quit()
            self._driver = None

        type(self).clear_instance()
