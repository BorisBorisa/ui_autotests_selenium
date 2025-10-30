from pydantic import BaseModel


class TestCase1(BaseModel):
    click_alert: str
    confirm_alert: str


class TestCase2(BaseModel):
    parent_frame_text: str
    nested_frame_text: str


class TestCase4(BaseModel):
    sample_page_url: str


class TestData(BaseModel):
    test_case1: TestCase1
    test_case2: TestCase2
    test_case4: TestCase4
