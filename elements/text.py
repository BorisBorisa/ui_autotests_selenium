import allure

from elements.base_element import BaseElement

from tools.webdriver.waiter import Waiter
from tools.logger import get_logger

logger = get_logger("TEXT")


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"

    def get_inner_text(self, **kwargs) -> str:
        locator = self.get_locator(**kwargs)
        step = f'Getting {self.type_of} "{self.name}" inner text'

        with allure.step(step):
            logger.info(step)
            element = Waiter.visible(locator)
            return element.text
