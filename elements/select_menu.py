from elements.base_element import BaseElement

from tools.webdriver.waiter import Waiter
from selenium.webdriver.support.select import Select


class SelectMenu(BaseElement):
    def type_of(self) -> str:
        return "select"

    def select_by_text(self, text: str):
        locator = self.get_locator()
        element = Waiter.visible(locator)
        Select(element).select_by_visible_text(text)
