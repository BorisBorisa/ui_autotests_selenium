from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent

from elements.text import Text
from elements.button import Button


class BrowserWindowsPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="browserWindows"]/h1')

        self.new_tab_button = Button("new tab", By.ID, "tabButton")
        self.new_window_button = Button("new window", By.ID, "windowButton")
        self.new_window_message_button = Button("new window message", By.ID, "messageWindowButton")

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Browser Windows")
