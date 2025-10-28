import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.alerts_frame_windows.nested_frame_component import NestedFrameComponent

from elements.text import Text


class NestedFramesPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="framesWrapper"]/h1')

        self.nested_frame = NestedFrameComponent(
            frame_locator=(By.ID, "frame1"),
            nested_frame_locator=(By.XPATH, "//iframe")
        )

    @allure.step("Check Nested Frames page is opened")
    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Nested Frames")
