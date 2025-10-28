import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.widgets.slider_component import SliderComponent

from elements.text import Text


class SliderPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//h1')

        self.slider = SliderComponent()

    @allure.step("Check Slider page is opened")
    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Slider")

    @allure.step("Check slider input value matches expected {expected_value}")
    def check_slider_input_value_matches_expected(self, expected_value: int):
        actual_value = self.slider.get_value()

        assert actual_value == expected_value, (
            f'Slider input value mismatch: expected "{expected_value}", got "{actual_value}"'
        )
