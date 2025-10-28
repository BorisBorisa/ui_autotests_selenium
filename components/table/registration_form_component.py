import allure

from elements.text import Text
from elements.input import Input
from elements.button import Button

from tools.schemas.web_table_row_model import WebTableRow


class RegistrationFormComponent:
    def __init__(self):
        self.title = Text("title", "id", "registration-form-modal")

        self.first_name_input = Input("first name", "id", "firstName")
        self.last_name_input = Input("last name", "id", "lastName")
        self.email_input = Input("email", "id", "userEmail")
        self.age_input = Input("age", "id", "age")
        self.salary_input = Input("salary", "id", "salary")
        self.department_input = Input("department", "id", "department")

        self.close_button = Button("close", "xpath", '//button[@class="close"]')
        self.submit_button = Button("submit", "id", "submit")

    @allure.step("Check registration form is opened")
    def is_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Registration Form")

    @allure.step("Fill registration form")
    def fill(self, user_data: WebTableRow):
        self.first_name_input.fill(user_data.first_name)
        self.last_name_input.fill(user_data.last_name)
        self.email_input.fill(user_data.email)
        self.age_input.fill(user_data.age)
        self.salary_input.fill(user_data.salary)
        self.department_input.fill(user_data.department)

    def click_close_button(self):
        self.close_button.click()

    def click_submit_button(self):
        self.submit_button.click()
