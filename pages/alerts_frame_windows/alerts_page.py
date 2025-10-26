from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent

from elements.text import Text
from elements.button import Button

from tools.browser_alert import BrowserAlert


class AlertsPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="javascriptAlertsWrapper"]/h1')

        self.alert_button = Button("alert", By.ID, "alertButton")
        self.timer_alert_button = Button("timer alert", By.ID, "timerAlertButton")
        self.confirm_button = Button("confirm", By.ID, "confirmButton")
        self.prompt_button = Button("prompt", By.ID, "promtButton")

        self.confirm_result = Text("confirm result", By.ID, "confirmResult")
        self.prompt_result = Text("prompt result", By.ID, "promptResult")

        self.browser_alert = BrowserAlert()

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Alerts")

    def click_alert_button(self):
        self.alert_button.click()

    def click_timer_alert_button(self):
        self.timer_alert_button.click()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_prompt_button(self):
        self.prompt_button.click()

    def check_confirm_result_text(self):
        self.confirm_result.check_have_text("You selected Ok")

    def check_prompt_result_text(self, text: str):
        self.prompt_result.check_have_text(f"You entered {text}")
