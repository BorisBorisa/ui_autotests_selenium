from enum import StrEnum


class Elements(StrEnum):
    TEXT_BOX = "Text Box"
    CHECK_BOX = "Check Box"
    RADIO_BUTTON = "Radio Button"
    WEB_TABLES = "Web Tables"
    BUTTONS = "Buttons"
    LINKS = "Links"
    BROKEN_LINKS_IMAGES = "Broken Links - Images"
    UPLOAD_AND_DOWNLOAD = "Upload and Download"
    DYNAMIC_PROPERTIES = "Dynamic Properties"


class Forms(StrEnum):
    PRACTICE_FORM = "Practice Form"


class AlertsFrameWindows(StrEnum):
    BROWSER_WINDOWS = "Browser Windows"
    ALERTS = "Alerts"
    FRAMES = "Frames"
    NESTED_FRAMES = "Nested Frames"
    MODAL_DIALOGS = "Modal Dialogs"


class Widgets(StrEnum):
    ACCORDIAN = "Accordian"
    AUTO_COMPLETE = "Auto Complete"
    DATE_PICKER = "Date Picker"
    SLIDER = "Slider"
    PROGRESS_BAR = "Progress Bar"
    TABS = "Tabs"
    TOOL_TIPS = "Tool Tips"
    MENU = "Menu"
    SELECT_MENU = "Select Menu"


class Interactions(StrEnum):
    SORTABLE = "Sortable"
    SELECTABLE = "Selectable"
    RESIZABLE = "Resizable"
    DROPPABLE = "Droppable"
    DRAGGABLE = "Draggable"


class BookStoreApplication(StrEnum):
    LOGIN = "Login"
    BOOK_STORE = "Book Store"
    PROFILE = "Profile"
    BOOK_STORE_API = "Book Store API"
