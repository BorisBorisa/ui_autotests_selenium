import allure

from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent
from components.navigation.left_panel_component import LeftPanelComponent
from components.table.registration_form_component import RegistrationFormComponent
from components.table.table_component import TableComponent

from elements.text import Text
from elements.input import Input
from elements.button import Button


class WebTablesPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.left_panel = LeftPanelComponent()

        self.title = Text("title", "xpath", '//h1[@class="text-center"]')

        self.add_button = Button("add", "id", "addNewRecordButton")
        self.search_input = Input("search", "id", "searchBox")

        self.registration_form = RegistrationFormComponent()
        self.table = TableComponent()

    @allure.step("Check Web Tables page is opened")
    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Web Tables")

    def click_add_button(self):
        self.add_button.click()
