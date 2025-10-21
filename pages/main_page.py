from pages.base_page import BasePage

from components.navigation.header_component import HeaderComponent

from elements.button import Button

from tools.enums.category_enum import Category


class MainPage(BasePage):
    def __init__(self):
        super().__init__()

        self.header = HeaderComponent()
        self.category_card_button = Button("category card", "xpath", '//*[@class="category-cards"]//*[text()="{text}"]')

    def click_elements_button(self):
        self.category_card_button.click(text=Category.ELEMENTS)

    def click_forms_button(self):
        self.category_card_button.click(text=Category.FORMS)

    def click_alerts_frame_windows_button(self):
        self.category_card_button.click(text=Category.ALERTS_FRAME_WINDOWS)

    def click_widgets_button(self):
        self.category_card_button.click(text=Category.WIDGETS)

    def click_interactions_button(self):
        self.category_card_button.click(text=Category.INTERACTIONS)

    def click_book_store_application_button(self):
        self.category_card_button.click(text=Category.BOOK_STORE_APPLICATION)
