import allure
import pytest

from pages.main_page import MainPage
from pages.alerts_frame_windows.alerts_page import AlertsPage

from tools.fakers import fake
from tools.allure.epics import AllureEpic

from config import settings

test_data = settings.test_data.test_case1


@allure.epic(AllureEpic.ALERTS_FRAMES_WINDOWS)
@pytest.mark.alert
class TestCase1:
    def test_alerts(self, main_page: MainPage, alerts_page: AlertsPage):
        main_page.visit(settings.get_base_url())
        main_page.is_page_opened()

        main_page.click_alerts_frame_windows_button()
        alerts_page.left_panel.alerts_frames_windows.click_alerts_menu_item()
        alerts_page.is_page_opened()

        alerts_page.click_alert_button()
        alerts_page.browser_alert.check_alert_text(test_data.click_alert)
        alerts_page.browser_alert.accept_alert()
        alerts_page.browser_alert.alert_is_closed()

        alerts_page.click_confirm_button()
        alerts_page.browser_alert.check_alert_text(test_data.confirm_alert)
        alerts_page.browser_alert.accept_alert()
        alerts_page.browser_alert.alert_is_closed()
        alerts_page.check_confirm_result_text()

        test_value = fake.word()

        alerts_page.click_prompt_button()
        alerts_page.browser_alert.send_text_to_alert(test_value)
        alerts_page.browser_alert.accept_alert()
        alerts_page.browser_alert.alert_is_closed()
        alerts_page.check_prompt_result_text(test_value)
