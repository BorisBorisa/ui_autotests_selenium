import allure

from datetime import datetime
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.date_picker.date_picker_input_component import DatePickerComponent
from components.date_picker.date_time_picker_input_component import DateTimePickerComponent

from elements.text import Text


class DatePickerPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="datePickerContainer"]/h1')

        self.date_picker = DatePickerComponent()
        self.date_time_picker = DateTimePickerComponent()

    @allure.step("Check Date picker page is opened")
    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Date Picker")

    def check_displayed_date_is_current(self):
        date_time = datetime.now()

        self.date_picker.check_current_date_matches_expected(date_time)
        self.date_time_picker.check_current_date_matches_expected(date_time)
