import allure

from datetime import date, datetime
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent

from elements.select_menu import SelectMenu
from elements.input import Input
from elements.text import Text


class DatePickerComponent(BaseComponent):
    def __init__(self):
        super().__init__()

        self.date_picker_input = Input("date picker", By.ID, 'datePickerMonthYearInput')

        self.month_select_menu = SelectMenu("month", By.CLASS_NAME, "react-datepicker__month-select")
        self.year_select_menu = SelectMenu("year", By.CLASS_NAME, "react-datepicker__year-select")

        self.day = Text("day", By.XPATH, '//*[@class = "react-datepicker__month"]/*[{week_index}]/*[{day_index}]')

    def click_date_picker_input(self):
        self.date_picker_input.click()

    @allure.step("Set date via input: {date_str}")
    def set_data_by_input(self, date_str: str):
        self.date_picker_input.clear()
        self.date_picker_input.fill(date_str)

    @allure.step("Get selected date from input")
    def get_selected_date(self) -> date:
        value = self.date_picker_input.get_attr("value")
        return datetime.strptime(value, "%m/%d/%Y").date()

    @allure.step("Select date {target_date:%d %B %Y} via calendar")
    def select_date_via_calendar(self, target_date: datetime):
        self.click_date_picker_input()

        self.month_select_menu.select_by_text(target_date.strftime("%B"))
        self.year_select_menu.select_by_text(str(target_date.year))

        week_index = target_date.isocalendar()[1] - target_date.replace(day=1).isocalendar()[1] + 1
        day_index = target_date.weekday() + 2
        self.day.click(week_index=week_index, day_index=day_index)

    @allure.step("Check that selected date equals expected date {expected_date:%d %B %Y}")
    def check_current_date_matches_expected(self, expected_date: datetime):
        actual_date = self.get_selected_date()
        expected_date = expected_date.date()

        assert actual_date == expected_date, (
            f'Selected date {actual_date} does not match expected date {expected_date}'
        )
