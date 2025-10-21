from components.navigation.element_group_component import (
    ElementsGroupComponent,
    FormsGroupComponent,
    AlertsFramesWindowsGroupComponent,
    WidgetsGroupComponent,
    InteractionsGroupComponent,
    BookStoreApplicationGroupComponent
)


class LeftPanelComponent:
    def __init__(self):
        super().__init__()

        self.elements = ElementsGroupComponent()
        self.forms = FormsGroupComponent()
        self.alerts_frames_windows = AlertsFramesWindowsGroupComponent()
        self.widgets = WidgetsGroupComponent()
        self.interactions = InteractionsGroupComponent()
        self.books_store_application = BookStoreApplicationGroupComponent()
