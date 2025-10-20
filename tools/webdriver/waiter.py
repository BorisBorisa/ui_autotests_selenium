from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.webdriver.driver_manager import driver
from config import settings


class Waiter:
    @staticmethod
    def _wait():
        return WebDriverWait(
            driver=driver(),
            timeout=settings.browsers_config.wait_timeout,
            poll_frequency=settings.browsers_config.wait_poll_frequency
        )

    @staticmethod
    def visible(locator):
        return Waiter._wait().until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def clickable(locator):
        return Waiter._wait().until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def have_text(locator, text):
        return Waiter._wait().until(
            EC.text_to_be_present_in_element(locator, text)
        )
