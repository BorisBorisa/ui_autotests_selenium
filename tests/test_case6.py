import allure
import pytest

from pages.main_page import MainPage
from pages.widgets.date_picker_page import DatePickerPage

from config import settings
from tools.fakers import fake
from tools.allure.epics import AllureEpic


@allure.epic(AllureEpic.WIDGETS)
@pytest.mark.widget
@pytest.mark.date_picker
class TestCase6:
    def test_date_picker(self, main_page: MainPage, date_picker_page: DatePickerPage):
        main_page.visit(settings.get_base_url())
        main_page.is_page_opened()

        main_page.click_widgets_button()
        date_picker_page.left_panel.widgets.click_date_picker_menu_item()
        date_picker_page.is_page_opened()

        date_picker_page.check_displayed_date_is_current()

        test_date = fake.data_time()

        date_picker_page.date_picker.select_date_via_calendar(test_date)
        date_picker_page.date_picker.check_current_date_matches_expected(test_date)
