from elements.base_element import BaseElement

from selenium.webdriver.common.by import ByType

from tools.webdriver.waiter import Waiter


class Input(BaseElement):
    def __init__(self, name: str, locator_type: ByType, locator: str):
        super().__init__(name, locator_type, locator)

    def type_of(self) -> str:
        return "input"

    def fill(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        element = Waiter.clickable(locator)
        element.send_keys(text)
