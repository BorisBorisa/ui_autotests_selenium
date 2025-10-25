from elements.base_element import BaseElement

from tools.webdriver.waiter import Waiter


class Text(BaseElement):
    def type_of(self) -> str:
        return "text"

    def get_inner_text(self, **kwargs) -> str:
        locator = self.get_locator(**kwargs)
        element = Waiter.visible(locator)
        return element.text
