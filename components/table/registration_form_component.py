from elements.text import Text
from elements.input import Input
from elements.button import Button


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

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Registration Form")

    def fill(
            self,
            first_name: str,
            last_name: str,
            email: str,
            age: int,
            salary: str,
            department: str
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.age_input.fill(str(age))
        self.salary_input.fill(salary)
        self.department_input.fill(department)

    def click_close_button(self):
        self.close_button.click()

    def click_submit_button(self):
        self.submit_button.click()
