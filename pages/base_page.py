import allure

from tools.webdriver.driver_manager import driver
from tools.webdriver.waiter import Waiter


class BasePage:
    def __init__(self):
        pass

    @staticmethod
    def visit(url: str):
        step = f"Opening the url '{url}'"

        with allure.step(step):
            driver().get(url)

    @staticmethod
    def reload():
        url = driver().current_url
        step = f"Reloading page with url '{url}'"

        with allure.step(step):
            driver().refresh()

    @staticmethod
    def check_current_url(expected_url: str):
        step = f'Checking that current url matches "{expected_url}"'

        with allure.step(step):
            Waiter.url_matches(expected_url)
