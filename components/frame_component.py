from contextlib import contextmanager

from tools.webdriver.driver_manager import driver
from tools.webdriver.waiter import Waiter

from elements.text import Text


class FrameComponent:
    def __init__(self, locator: tuple[str, str]):
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

    def check_heading_text(self, expected_text: str):
        with self.in_frame():
            self.heading.check_have_text(expected_text)

    def get_heading_text(self) -> str:
        with self.in_frame():
            return self.heading.get_inner_text()
