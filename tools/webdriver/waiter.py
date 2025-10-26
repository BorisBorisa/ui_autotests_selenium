from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.webdriver.custom_expected_conditions import text_to_be_equal_to_element_attribute
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
    def visible(locator) -> WebElement:
        return Waiter._wait().until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def clickable(locator) -> WebElement:
        return Waiter._wait().until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def have_text(locator, text):
        Waiter._wait().until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @staticmethod
    def have_attr(locator, attr):
        Waiter._wait().until(
            EC.element_attribute_to_include(locator, attr)
        )

    @staticmethod
    def have_attr_text(locator, attr, text):
        element = driver().find_element(*locator)

        WebDriverWait(driver(), 15, 0.05).until(
            text_to_be_equal_to_element_attribute(element, attr, text)
        )

    @staticmethod
    def url_matches(pattern: str):
        Waiter._wait().until(
            EC.url_matches(pattern)
        )

    @staticmethod
    def alert_is_present() -> Alert:
        return Waiter._wait().until(
            EC.alert_is_present()
        )
