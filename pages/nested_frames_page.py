from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.nested_frame_component import NestedFrameComponent

from elements.text import Text


class NestedFramesPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", "xpath", '//*[@id="framesWrapper"]/h1')

        self.nested_frame = NestedFrameComponent(
            frame_locator=("id", "frame1"),
            nested_frame_locator=("xpath", "//iframe")
        )

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Nested Frames")
