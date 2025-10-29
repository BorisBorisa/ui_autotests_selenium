from tools.webdriver.driver_manager import driver


class BrowserWindows:
    @staticmethod
    def get_all_handles() -> list[str]:
        return driver().window_handles

    @staticmethod
    def get_current_handle() -> str:
        return driver().current_window_handle

    @staticmethod
    def switch_to(index_or_handle):
        if isinstance(index_or_handle, int):
            driver().switch_to.window(BrowserWindows.get_all_handles()[index_or_handle])
        else:
            driver().switch_to.window(index_or_handle)

    @staticmethod
    def switch_to_last_tab():
        last_tab = BrowserWindows.get_all_handles()[-1]
        BrowserWindows.switch_to(last_tab)

    @staticmethod
    def close_current_tab():
        driver().close()
