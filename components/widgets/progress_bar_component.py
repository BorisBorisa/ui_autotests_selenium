from selenium.webdriver.common.by import By

from tools.webdriver.driver_manager import driver
from tools.webdriver.waiter import Waiter


class ProgressBarComponent:
    def __init__(self):
        self.start_stop_button_locator = (By.ID, "startStopButton")

        self.bar_value_locator = (By.XPATH, '//*[@id="progressBar"]/*')
        self.bar_value_attr = "aria-valuenow"

    def set_progres_bar_to(self, value: int):
        btn_elem = driver().find_element(*self.start_stop_button_locator)
        bar_val_elem = driver().find_element(*self.bar_value_locator)

        if bar_val_elem.get_attribute(self.bar_value_attr) == str(value):
            return

        btn_elem.click()
        Waiter.have_attr_text(self.bar_value_locator, self.bar_value_attr, str(value))
        btn_elem.click()

    def get_value(self) -> int:
        bar_val_elem = driver().find_element(*self.bar_value_locator)
        return int(bar_val_elem.get_attribute(self.bar_value_attr))
