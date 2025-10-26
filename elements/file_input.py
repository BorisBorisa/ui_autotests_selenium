from elements.base_element import BaseElement
from tools.webdriver.waiter import Waiter


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str, **kwargs):
        locator = self.get_locator(**kwargs)
        element = Waiter.clickable(locator)
        element.send_keys(file)
