from elements.base_element import BaseElement

from selenium.webdriver.common.by import ByType


class Button(BaseElement):
    def __init__(self, name: str, locator_type: ByType, locator: str):
        super().__init__(name, locator_type, locator)

    def type_of(self) -> str:
        return "button"
