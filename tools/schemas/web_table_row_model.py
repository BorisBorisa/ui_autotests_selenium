from pydantic import BaseModel
from functools import total_ordering


@total_ordering
class WebTableRow(BaseModel):
    first_name: str
    last_name: str
    age: str
    email: str
    salary: str
    department: str
    index: int | None = None

    def __eq__(self, other):
        if not isinstance(other, WebTableRow):
            return NotImplemented
        return all((
            self.first_name == other.first_name,
            self.last_name == other.last_name,
            self.age == other.age,
            self.email == other.email,
            self.salary == other.salary,
            self.department == other.department,
        ))

    def __lt__(self, other):
        if not isinstance(other, WebTableRow):
            return NotImplemented
        return ((self.last_name, self.first_name, self.age, self.email, self.salary, self.department) <
                (other.last_name, other.first_name, other.age, other.email, other.salary, other.department))
