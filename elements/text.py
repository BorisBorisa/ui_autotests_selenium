from elements.base_element import BaseElement

from selenium.webdriver.common.by import ByType

from tools.webdriver.waiter import Waiter


class Text(BaseElement):
    def __init__(self, name: str, locator_type: ByType, locator: str):
        super().__init__(name, locator_type, locator)

    def type_of(self) -> str:
        return "text"

    def get_inner_text(self, **kwargs) -> str:
        locator = self.get_locator(**kwargs)
        element = Waiter.visible(locator)
        return element.text
