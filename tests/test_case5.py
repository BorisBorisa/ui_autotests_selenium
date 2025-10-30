import pytest

from pages.main_page import MainPage
from pages.widgets.slider_page import SliderPage
from pages.widgets.progress_bar_page import ProgressBarPage

from tools.fakers import fake

from config import settings

@pytest.mark.widget
@pytest.mark.slider
@pytest.mark.progress_bar
class TestCase5:
    def test(self, main_page: MainPage, slider_page: SliderPage, progress_bar_page: ProgressBarPage):
        main_page.visit(settings.get_base_url())
        main_page.is_page_opened()

        main_page.click_widgets_button()
        slider_page.left_panel.widgets.click_slider_menu_item()
        slider_page.is_page_opened()

        random_int = fake.integer()

        slider_page.slider.set_slider_to(random_int)
        slider_page.check_slider_input_value_matches_expected(random_int)

        slider_page.left_panel.widgets.click_progress_bar_menu_item()
        progress_bar_page.is_page_opened()

        progress_bar_page.progress_bar.set_progres_bar_to(random_int)
        progress_bar_page.check_progress_bar_value_matches_expected(random_int)
