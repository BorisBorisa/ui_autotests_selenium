import allure

from abc import ABC, abstractmethod
from typing import Type
from enum import Enum

from elements.text import Text
from elements.button import Button

from tools.enums.category_enum import Category
from tools.enums.menu_enums import Elements, Forms, AlertsFrameWindows, Widgets, Interactions, BookStoreApplication


class BaseElementGroupComponent(ABC):
    def __init__(self):
        super().__init__()

        self.group_header = Text(
            "group header",
            "xpath",
            '//*[text()="{header_text}"]/ancestor::*[@class="header-wrapper"]'
        )
        self.group_element_item = Button(
            "group element",
            "xpath",
            '//*[text()="{button_text}"]/parent::*[contains(@class, "btn")]'
        )

    def check_visible(self, menu_elements: Type[Enum]):
        for i in menu_elements:
            self.group_element_item.check_visible(button_text=i)

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def check_menu_visible(self):
        pass


class ElementsGroupComponent(BaseElementGroupComponent):
    def click(self):
        self.group_header.click(header_text=Category.ELEMENTS)

    @allure.step("Check elements menu items visible")
    def check_menu_visible(self):
        self.check_visible(Elements)

    def click_text_box_menu_item(self):
        self.group_element_item.click(button_text=Elements.TEXT_BOX)

    def click_check_box_menu_item(self):
        self.group_element_item.click(button_text=Elements.CHECK_BOX)

    def click_radio_button_menu_item(self):
        self.group_element_item.click(button_text=Elements.RADIO_BUTTON)

    def click_web_tables_menu_item(self):
        self.group_element_item.click(button_text=Elements.WEB_TABLES)

    def click_buttons_menu_item(self):
        self.group_element_item.click(button_text=Elements.BUTTONS)

    def click_links_menu_item(self):
        self.group_element_item.click(button_text=Elements.LINKS)

    def click_broken_links_images_menu_item(self):
        self.group_element_item.click(button_text=Elements.BROKEN_LINKS_IMAGES)

    def click_upload_and_download_menu_item(self):
        self.group_element_item.click(button_text=Elements.UPLOAD_AND_DOWNLOAD)

    def click_dynamic_properties_menu_item(self):
        self.group_element_item.click(button_text=Elements.DYNAMIC_PROPERTIES)


class FormsGroupComponent(BaseElementGroupComponent):
    def click(self):
        self.group_header.click(header_text=Category.FORMS)

    @allure.step("Check forms group menu items visible")
    def check_menu_visible(self):
        self.check_visible(Forms)

    def click_practice_form_menu_item(self):
        self.group_element_item.click(button_text=Forms.PRACTICE_FORM)


class AlertsFramesWindowsGroupComponent(BaseElementGroupComponent):
    def click(self):
        self.group_header.click(header_text=Category.ALERTS_FRAME_WINDOWS)

    @allure.step("Check alerts frames and windows menu items visible")
    def check_menu_visible(self):
        self.check_visible(AlertsFrameWindows)

    def click_browser_windows_menu_item(self):
        self.group_element_item.click(button_text=AlertsFrameWindows.BROWSER_WINDOWS)

    def click_alerts_menu_item(self):
        self.group_element_item.click(button_text=AlertsFrameWindows.ALERTS)

    def click_frames_menu_item(self):
        self.group_element_item.click(button_text=AlertsFrameWindows.FRAMES)

    def click_nested_frames_menu_item(self):
        self.group_element_item.click(button_text=AlertsFrameWindows.NESTED_FRAMES)

    def click_modal_dialogs_menu_item(self):
        self.group_element_item.click(button_text=AlertsFrameWindows.MODAL_DIALOGS)


class WidgetsGroupComponent(BaseElementGroupComponent):
    def click(self):
        self.group_header.click(header_text=Category.WIDGETS)

    @allure.step("Check widgets menu items visible")
    def check_menu_visible(self):
        self.check_visible(Widgets)

    def click_accordian_menu_item(self):
        self.group_element_item.click(button_text=Widgets.ACCORDIAN)

    def click_auto_complete_menu_item(self):
        self.group_element_item.click(button_text=Widgets.AUTO_COMPLETE)

    def click_date_picker_menu_item(self):
        self.group_element_item.click(button_text=Widgets.DATE_PICKER)

    def click_slider_menu_item(self):
        self.group_element_item.click(button_text=Widgets.SLIDER)

    def click_progress_bar_menu_item(self):
        self.group_element_item.click(button_text=Widgets.PROGRESS_BAR)

    def click_tabs_menu_item(self):
        self.group_element_item.click(button_text=Widgets.TABS)

    def click_tool_tips_menu_item(self):
        self.group_element_item.click(button_text=Widgets.TOOL_TIPS)

    def click_menu_menu_item(self):
        self.group_element_item.click(button_text=Widgets.MENU)

    def click_select_menu_menu_item(self):
        self.group_element_item.click(button_text=Widgets.SELECT_MENU)


class InteractionsGroupComponent(BaseElementGroupComponent):
    def click(self):
        self.group_header.click(header_text=Category.INTERACTIONS)

    @allure.step("Check interactions group menu items visible")
    def check_menu_visible(self):
        self.check_visible(Interactions)

    def click_sortable_menu_item(self):
        self.group_element_item.click(button_text=Interactions.SORTABLE)

    def click_selectable_menu_item(self):
        self.group_element_item.click(button_text=Interactions.SELECTABLE)

    def click_resizable_menu_item(self):
        self.group_element_item.click(button_text=Interactions.RESIZABLE)

    def click_droppable_menu_item(self):
        self.group_element_item.click(button_text=Interactions.DROPPABLE)

    def click_draggable_menu_item(self):
        self.group_element_item.click(button_text=Interactions.DRAGGABLE)


class BookStoreApplicationGroupComponent(BaseElementGroupComponent):
    def click(self):
        self.group_header.click(header_text=Category.BOOK_STORE_APPLICATION)

    @allure.step("Check bookstore application menu items visible")
    def check_menu_visible(self):
        self.check_visible(BookStoreApplication)

    def click_login_menu_item(self):
        self.group_element_item.click(button_text=BookStoreApplication.LOGIN)

    def click_book_store_menu_item(self):
        self.group_element_item.click(button_text=BookStoreApplication.BOOK_STORE)

    def click_profile_menu_item(self):
        self.group_element_item.click(button_text=BookStoreApplication.PROFILE)

    def click_book_store_api_menu_item(self):
        self.group_element_item.click(button_text=BookStoreApplication.BOOK_STORE_API)
