from elements.base_element import BaseElement
from tools.webdriver.waiter import Waiter


class Input(BaseElement):
    def type_of(self) -> str:
        return "input"

    def fill(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        element = Waiter.clickable(locator)
        element.send_keys(text)
