from abc import ABC, abstractmethod

from selenium.webdriver.common.by import ByType

from tools.webdriver.waiter import Waiter
from tools.webdriver.driver_manager import driver


class BaseElement(ABC):
    def __init__(self, name: str, locator_type: ByType, locator: str):
        self.name = name
        self.locator_type = locator_type
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        pass

    def get_locator(self, **kwargs) -> tuple[ByType, str]:
        locator = self.locator.format(**kwargs)
        return self.locator_type, locator

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        element = Waiter.clickable(locator)
        element.click()

    def check_visible(self, **kwargs):
        locator = self.get_locator(**kwargs)
        Waiter.visible(locator)

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        Waiter.have_text(locator, text)

    def get_attr(self, attr: str, **kwargs) -> str | None:
        locator = self.get_locator(**kwargs)
        Waiter.have_attr(locator, attr)
        return driver().find_element(*locator).get_attribute(attr)
