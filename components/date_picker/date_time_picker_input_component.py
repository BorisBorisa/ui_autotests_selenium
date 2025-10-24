from datetime import datetime

from selenium.webdriver.common.by import By

from elements.input import Input


class DateTimePickerComponent:
    def __init__(self):
        self.date_picker_input = Input("date picker", By.ID, 'dateAndTimePickerInput')

    def open_calendar(self):
        self.date_picker_input.click()

    def set_data_by_input(self, date_str: str):
        self.date_picker_input.clear()
        self.date_picker_input.fill(date_str)

    def get_selected_date(self) -> datetime:
        value = self.date_picker_input.get_attr("value")
        return datetime.strptime(value, "%B %d, %Y %I:%M %p")

    def check_current_date_matches_expected(self, expected_date: datetime):
        actual_date = self.get_selected_date()
        expected_date = expected_date.replace(second=0, microsecond=0)
        assert actual_date == expected_date, (
            f'Selected date {actual_date} does not match expected date {expected_date}'
        )
