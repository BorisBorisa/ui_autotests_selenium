from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent

from elements.text import Text
from elements.link import Link


class LinksPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", By.XPATH, '//*[@id="linkWrapper"]/h1')
        self.home_link = Link("home", By.ID, "simpleLink")

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Links")

    def click_home_link(self):
        self.home_link.click()
