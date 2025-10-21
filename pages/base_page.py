from tools.webdriver.driver_manager import driver
from tools.webdriver.waiter import Waiter


class BasePage:
    def __init__(self):
        pass

    @staticmethod
    def visit(url: str):
        driver().get(url)

    @staticmethod
    def reload():
        driver().refresh()

    @staticmethod
    def check_current_url(expected_url: str):
        Waiter.url_matches(expected_url)
