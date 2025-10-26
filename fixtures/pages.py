import pytest

from pages.main_page import MainPage
from pages.sample_page import SamplePage

from pages.alerts_frame_windows.alerts_page import AlertsPage
from pages.alerts_frame_windows.browser_windows_page import BrowserWindowsPage
from pages.alerts_frame_windows.frames_page import FramesPage
from pages.alerts_frame_windows.nested_frames_page import NestedFramesPage

from pages.elements.links_page import LinksPage
from pages.elements.web_tables_page import WebTablesPage

from pages.widgets.date_picker_page import DatePickerPage
from pages.widgets.progress_bar_page import ProgressBarPage
from pages.widgets.slider_page import SliderPage


@pytest.fixture
def main_page() -> MainPage:
    return MainPage()


@pytest.fixture
def sample_page() -> SamplePage:
    return SamplePage()


@pytest.fixture
def alerts_page() -> AlertsPage:
    return AlertsPage()


@pytest.fixture
def browser_windows_page() -> BrowserWindowsPage:
    return BrowserWindowsPage()


@pytest.fixture
def frames_page() -> FramesPage:
    return FramesPage()


@pytest.fixture
def nested_frames_page() -> NestedFramesPage:
    return NestedFramesPage()


@pytest.fixture
def links_page() -> LinksPage:
    return LinksPage()


@pytest.fixture
def web_tables_page() -> WebTablesPage:
    return WebTablesPage()


@pytest.fixture
def date_picker_page() -> DatePickerPage:
    return DatePickerPage()


@pytest.fixture
def progress_bar_page() -> ProgressBarPage:
    return ProgressBarPage()


@pytest.fixture
def slider_page() -> SliderPage:
    return SliderPage()
