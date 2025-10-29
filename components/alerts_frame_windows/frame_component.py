import allure

from contextlib import contextmanager

from tools.webdriver.driver_manager import driver
from tools.browser_tools.waiter import Waiter

from components.base_component import BaseComponent

from elements.text import Text


class FrameComponent(BaseComponent):
    def __init__(self, locator: tuple[str, str]):
        super().__init__()

        self.locator = locator
        self.heading = Text("heading", "id", "sampleHeading")

    @contextmanager
    def in_frame(self):
        frame = Waiter.visible(self.locator)
        driver().switch_to.frame(frame)
        try:
            yield
        finally:
            driver().switch_to.default_content()

    @allure.step('Check that frame heading text equal expected: "{expected_text}"')
    def check_heading_text(self, expected_text: str):
        with self.in_frame():
            self.heading.check_have_text(expected_text)

    @allure.step('Get heading text from frame')
    def get_heading_text(self) -> str:
        with self.in_frame():
            return self.heading.get_inner_text()
