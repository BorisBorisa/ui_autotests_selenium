import allure

from contextlib import contextmanager

from tools.webdriver.driver_manager import driver
from tools.browser_tools.waiter import Waiter

from components.base_component import BaseComponent

from elements.text import Text


class NestedFrameComponent(BaseComponent):
    def __init__(self, frame_locator: tuple[str, str], nested_frame_locator: tuple[str, str]):
        super().__init__()

        self.frame_locator = frame_locator
        self.nested_frame_locator = nested_frame_locator

        self.body_text = Text("body", "xpath", "//body")

    @contextmanager
    def in_frame(self, locator: tuple[str, str]):
        frame = Waiter.visible(locator)
        driver().switch_to.frame(frame)
        try:
            yield
        finally:
            driver().switch_to.default_content()

    @allure.step('Check that frame text equal expected: "{expected_text}"')
    def check_frame_text(self, expected_text: str):
        with self.in_frame(self.frame_locator):
            self.body_text.check_have_text(expected_text)

    @allure.step('Check that nested frame text equal expected: "{expected_text}"')
    def check_nested_frame_text(self, expected_text: str):
        with self.in_frame(self.frame_locator):
            with self.in_frame(self.nested_frame_locator):
                self.body_text.check_have_text(expected_text)
