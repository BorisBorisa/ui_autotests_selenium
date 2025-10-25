from selenium.webdriver.common.by import By

from tools.enums.column_header_enum import ColumnHeader
from tools.schemas.web_table_row_model import WebTableRow

from elements.button import Button

from tools.webdriver.driver_manager import driver


class TableComponent:
    def __init__(self):
        self.column_header = Button(
            "column header",
            By.XPATH,
            '//*[@role="columnheader"]/*[text()="{name}"]'
        )

        self.rows_locator = (By.XPATH, '//*[@class="rt-tbody"]//*[@role="row" and not(contains(@class, "-padRow"))]')
        self.rows_delete_button_locator = (By.XPATH, '//*[@class="rt-tbody"]//*[@title="Delete"]')

        self.row_delete_button = Button("delete row", By.ID, 'delete-record-{id}')

    def click_first_name_column_header(self):
        self.column_header.click(name=ColumnHeader.FIRST_NAME)

    def click_last_name_column_header(self):
        self.column_header.click(name=ColumnHeader.LAST_NAME)

    def click_age_column_header(self):
        self.column_header.click(name=ColumnHeader.AGE)

    def click_email_column_header(self):
        self.column_header.click(name=ColumnHeader.EMAIL)

    def click_salary_column_header(self):
        self.column_header.click(name=ColumnHeader.SALARY)

    def click_department_column_header(self):
        self.column_header.click(name=ColumnHeader.DEPARTMENT)

    def click_action_column_header(self):
        self.column_header.click(name=ColumnHeader.ACTION)

    def get_all_rows(self) -> list[WebTableRow]:
        rows = driver().find_elements(*self.rows_locator)
        rows_delete_buttons = driver().find_elements(*self.rows_delete_button_locator)

        result = []

        for idx, row in enumerate(rows):
            user_id = int(rows_delete_buttons[idx].get_attribute("id").split("-")[-1])

            row_text = row.text.split("\n")
            f_name, l_name, age, email, salary, department = row_text

            result.append(WebTableRow(
                user_id=user_id,
                first_name=f_name,
                last_name=l_name,
                email=email,
                age=age,
                salary=salary,
                department=department
            ))

        return result

    def user_in_table(self, user: WebTableRow) -> bool:
        rows = self.get_all_rows()
        return user in rows

    def check_user_present_in_table(self, user: WebTableRow):
        assert self.user_in_table(user)

    def assert_user_not_present_in_table(self, user: WebTableRow):
        assert not self.user_in_table(user)

    def delete_row(self, row_id: int):
        self.row_delete_button.click(id=row_id)
