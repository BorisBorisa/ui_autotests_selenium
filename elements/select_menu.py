import allure

from selenium.webdriver.support.select import Select

from elements.base_element import BaseElement

from tools.webdriver.waiter import Waiter
from tools.logger import get_logger

logger = get_logger("SELECT_MENU")


class SelectMenu(BaseElement):
    @property
    def type_of(self) -> str:
        return "select"

    def select_by_text(self, text: str):
        locator = self.get_locator()
        step = f'Select "{text}" from {self.type_of} "{self.name}"'

        with allure.step(step):
            logger.info(step)
            element = Waiter.visible(locator)
            Select(element).select_by_visible_text(text)
