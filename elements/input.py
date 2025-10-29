import allure

from elements.base_element import BaseElement

from tools.webdriver.waiter import Waiter
from tools.logger import get_logger

logger = get_logger("INPUT")


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            logger.info(step)
            element = Waiter.clickable(locator)
            element.send_keys(value)

    def clear(self, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Clear {self.type_of} "{self.name}"'

        with allure.step(step):
            logger.info(step)
            element = Waiter.clickable(locator)
            element.clear()
