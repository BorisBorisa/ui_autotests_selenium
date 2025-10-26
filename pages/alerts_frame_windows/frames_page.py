from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.frame_component import FrameComponent

from elements.text import Text


class FramesPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", "xpath", '//*[@id="framesWrapper"]/h1')

        self.frame1 = FrameComponent(("id", "frame1"))
        self.frame2 = FrameComponent(("id", "frame2"))

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Frames")

    def check_frames_headings_are_equal(self):
        frame1_text = self.frame1.get_heading_text()
        self.frame2.check_heading_text(frame1_text)
