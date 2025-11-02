from pydantic import BaseModel


class Case1(BaseModel):
    click_alert: str
    confirm_alert: str


class Case2(BaseModel):
    parent_frame_text: str
    nested_frame_text: str


class Case4(BaseModel):
    sample_page_url: str


class DataModel(BaseModel):
    test_case1: Case1
    test_case2: Case2
    test_case4: Case4
