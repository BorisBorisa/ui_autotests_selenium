from elements.link import Link


class HeaderComponent:
    def __init__(self):
        self.logo_link = Link("logo", "xpath", '//header/a')

    def click_logo(self):
        self.logo_link.click()
