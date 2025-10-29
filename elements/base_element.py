import allure

from abc import ABC, abstractmethod

from selenium.webdriver.common.by import ByType

from tools.browser_tools.waiter import Waiter
from tools.webdriver.driver_manager import driver
from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


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
        step = f'Getting locator "{locator}"'

        with allure.step(step):
            logger.info(step)
            return self.locator_type, locator

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Click {self.type_of} "{self.name}"'

        with allure.step(step):
            logger.info(step)
            element = Waiter.clickable(locator)
            element.click()

    def check_visible(self, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            logger.info(step)
            Waiter.visible(locator)

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            logger.info(step)
            Waiter.have_text(locator, text)

    def get_attr(self, attr: str, **kwargs) -> str | None:
        locator = self.get_locator(**kwargs)
        step = f'Getting {self.type_of} "{self.name}" attribute "{attr}" value'

        with allure.step(step):
            logger.info(step)
            Waiter.have_attr(locator, attr)
            return driver().find_element(*locator).get_attribute(attr)
