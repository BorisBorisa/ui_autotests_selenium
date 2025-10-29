import allure

from tools.browser_tools.waiter import Waiter
from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self):
        pass

    @staticmethod
    def check_current_url(expected_url: str):
        step = f"Check that current URL matches expected: '{expected_url}'"

        with allure.step(step):
            logger.info(step)
            Waiter.url_matches(expected_url)
