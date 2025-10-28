import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.widgets.progress_bar_component import ProgressBarComponent
from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent

from elements.text import Text
from elements.button import Button


class ProgressBarPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="progressBarContainer"]/h1')
        self.start_stop_button = Button("start stop", By.ID, "startStopButton")

        self.progress_bar = ProgressBarComponent()

    @allure.step("Check Progress bar page is opened")
    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Progress Bar")

    @allure.step("Check progress bar value matches expected {expected_value}")
    def check_progress_bar_value_matches_expected(self, expected_value: int):
        actual_value = self.progress_bar.get_value()

        assert actual_value == expected_value, (
            f'Bar value mismatch: expected "{expected_value}", got "{actual_value}"'
        )
