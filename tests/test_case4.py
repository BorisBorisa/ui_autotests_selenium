import pytest

from pages.main_page import MainPage
from pages.alerts_frame_windows.browser_windows_page import BrowserWindowsPage
from pages.sample_page import SamplePage
from pages.elements.links_page import LinksPage

from tools.browser_tools.browser_windows import BrowserWindows

from config import settings

test_data = settings.test_data.test_case4


@pytest.mark.element
@pytest.mark.window
@pytest.mark.link
class TestCase4:
    def test_handles(
            self,
            main_page: MainPage,
            browser_windows_page: BrowserWindowsPage,
            sample_page: SamplePage,
            links_page: LinksPage
    ):
        main_page.visit(settings.get_base_url())
        main_page.is_page_opened()

        main_page.click_alerts_frame_windows_button()
        browser_windows_page.left_panel.alerts_frames_windows.click_browser_windows_menu_item()
        browser_windows_page.is_page_opened()

        main_tab = BrowserWindows.get_current_handle()

        browser_windows_page.click_new_tab_button()
        BrowserWindows.switch_to_last_tab()

        sample_page.check_current_url(test_data.sample_page_url)
        sample_page.is_page_opened()

        BrowserWindows.close_current_tab()
        BrowserWindows.switch_to(main_tab)

        browser_windows_page.left_panel.elements.click()
        browser_windows_page.left_panel.elements.click_links_menu_item()
        links_page.is_page_opened()
        links_page.click_home_link()

        BrowserWindows.switch_to_last_tab()
        main_page.is_page_opened()

        BrowserWindows.switch_to(main_tab)
        links_page.is_page_opened()
