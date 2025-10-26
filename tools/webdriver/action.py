from selenium.webdriver import ActionChains
from tools.webdriver.driver_manager import driver


class Action:
    @staticmethod
    def _action():
        return ActionChains(
            driver=driver()
        )

    @staticmethod
    def drag_and_drop_by_offset(element, x, y):
        Action._action().drag_and_drop_by_offset(element, x, y).perform()
