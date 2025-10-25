from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from elements.text import Text

class SamplePage(BasePage):
    def __init__(self):
        super().__init__()

        self.title = Text("title", By.ID, "sampleHeading")

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("This is a sample page")
