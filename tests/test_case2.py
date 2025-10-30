import pytest

from pages.main_page import MainPage
from pages.alerts_frame_windows.nested_frames_page import NestedFramesPage
from pages.alerts_frame_windows.frames_page import FramesPage

from config import settings

test_data = settings.test_data.test_case2

@pytest.mark.frame
class TestCase2:
    def test_iframe(self, main_page: MainPage, nested_frames_page: NestedFramesPage, frames_page: FramesPage):
        main_page.visit(settings.get_base_url())
        main_page.is_page_opened()

        main_page.click_alerts_frame_windows_button()
        nested_frames_page.left_panel.alerts_frames_windows.click_nested_frames_menu_item()
        nested_frames_page.is_page_opened()

        nested_frames_page.nested_frame.check_parent_frame_text(test_data.parent_frame_text)
        nested_frames_page.nested_frame.check_nested_frame_text(test_data.nested_frame_text)

        nested_frames_page.left_panel.alerts_frames_windows.click_frames_menu_item()
        frames_page.is_page_opened()

        frames_page.check_frames_headings_are_equal()

