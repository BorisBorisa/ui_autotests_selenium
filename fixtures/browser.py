import pytest
from _pytest.fixtures import SubRequest

from tools.webdriver.driver_manager import DriverManger

from config import settings


@pytest.fixture(scope="session", autouse=True, params=settings.browsers)
def driver(request: SubRequest):
    DriverManger().init(request.param)
    yield
    DriverManger().close_driver()
