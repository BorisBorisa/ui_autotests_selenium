import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.alerts_frame_windows.frame_component import FrameComponent

from elements.text import Text


class FramesPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="framesWrapper"]/h1')

        self.frame1 = FrameComponent((By.ID, "frame1"))
        self.frame2 = FrameComponent((By.ID, "frame2"))

    @allure.step("Check Frames page is opened")
    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Frames")

    @allure.step("Check Frames headings are equal")
    def check_frames_headings_are_equal(self):
        frame1_text = self.frame1.get_heading_text()
        self.frame2.check_heading_text(frame1_text)
