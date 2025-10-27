from selenium.webdriver.common.by import By

from tools.webdriver.waiter import Waiter
from tools.webdriver.action import Action

from elements.input import Input


class SliderComponent:
    def __init__(self):
        self.slider = Input("slider", By.XPATH, '//*[@class="range-slider range-slider--primary"]')
        self.value = Input("value", By.ID, "sliderValue")

    def set_slider_to(self, value: int) -> None:
        element = Waiter.visible(self.slider.get_locator())

        slider_width = float(element.size["width"])
        min_range = float(element.get_attribute("min"))
        max_range = float(element.get_attribute("max"))

        percent = (value - min_range) / (max_range - min_range)

        offset = 10 - (20 * percent)
        zero_pos = (slider_width / 2) * -1
        position = round(zero_pos + offset + (slider_width * percent))

        Action.drag_and_drop_by_offset(element, position, 0)

    def get_value(self) -> int:
        value = self.value.get_attr("value")
        return int(value)
