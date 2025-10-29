import allure

from datetime import datetime

from selenium.webdriver.common.by import By

from elements.input import Input


class DateTimePickerComponent:
    def __init__(self):
        self.date_picker_input = Input("date picker", By.ID, 'dateAndTimePickerInput')

    def click_date_picker_input(self):
        self.date_picker_input.click()

    @allure.step("Set datetime via input: {date_str}")
    def set_data_by_input(self, date_str: str):
        self.date_picker_input.clear()
        self.date_picker_input.fill(date_str)

    @allure.step("Get selected datetime from input")
    def get_selected_datetime(self) -> datetime:
        value = self.date_picker_input.get_attr("value")
        return datetime.strptime(value, "%B %d, %Y %I:%M %p")

    @allure.step("Check that selected datetime equals expected datetime {expected_datetime}")
    def check_current_date_matches_expected(self, expected_datetime: datetime):
        actual_datetime = self.get_selected_datetime()
        expected_datetime = expected_datetime.replace(second=0, microsecond=0)
        assert actual_datetime == expected_datetime, (
            f'Selected date {actual_datetime} does not match expected date {expected_datetime}'
        )
