import allure
import pytest

from pages.main_page import MainPage
from pages.elements.web_tables_page import WebTablesPage

from tools.schemas.web_table_row_model import WebTableRow
from tools.allure.epics import AllureEpic

from config import settings


@allure.epic(AllureEpic.ELEMENTS)
@pytest.mark.element
@pytest.mark.table
class TestCase3:
    def test_tables(self, main_page: MainPage, web_tables_page: WebTablesPage):
        main_page.visit(settings.get_base_url())
        main_page.is_page_opened()

        main_page.click_elements_button()
        web_tables_page.left_panel.elements.click_web_tables_menu_item()
        web_tables_page.is_page_opened()

        user = WebTableRow()

        web_tables_page.click_add_button()
        web_tables_page.registration_form.is_opened()

        web_tables_page.registration_form.fill(user)
        web_tables_page.registration_form.click_submit_button()
        web_tables_page.table.check_user_present_in_table(user)

        web_tables_page.table.delete_user(user)
        web_tables_page.table.check_user_not_present_in_table(user)
