from typing import Callable

from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.common.exceptions import StaleElementReferenceException


def text_to_be_equal_to_element_attribute(
        element: WebElement,
        attribute: str,
        text: str
) -> Callable[[WebDriver], bool]:
    def _predicate(driver: WebDriver):
        try:
            element_text = element.get_attribute(attribute)
            if element_text is None:
                return False
            return text == element_text
        except StaleElementReferenceException:
            return False

    return _predicate
