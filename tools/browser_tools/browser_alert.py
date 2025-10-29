from selenium.common import NoAlertPresentException

from tools.webdriver.driver_manager import driver
from tools.browser_tools.waiter import Waiter


class BrowserAlert:
    @staticmethod
    def alert_is_closed() -> bool:
        try:
            return not driver().switch_to.alert
        except NoAlertPresentException:
            return True

    @staticmethod
    def accept_alert():
        Waiter().alert_is_present().accept()

    @staticmethod
    def dismiss_alert():
        Waiter().alert_is_present().dismiss()

    @staticmethod
    def send_text_to_alert(text) -> None:
        Waiter().alert_is_present().send_keys(text)

    @staticmethod
    def get_alert_text() -> str:
        return Waiter().alert_is_present().text

    def check_alert_text(self, expected_text: str):
        actual_text = self.get_alert_text()
        assert actual_text == expected_text, f"Expected alert text '{expected_text}', but got '{actual_text}'"
