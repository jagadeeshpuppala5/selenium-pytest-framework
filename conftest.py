import pytest

from pages.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from config.config import BASE_URL
from data.login_data import (
    VALID_USER,
    VALID_PASSWORD
)


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser Name"
    )


@pytest.fixture()
def driver(request):

    browser = request.config.getoption(
        "--browser"
    )

    driver = DriverFactory.get_driver(
        browser
    )

    yield driver

    driver.quit()


@pytest.fixture()
def login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        VALID_USER,
        VALID_PASSWORD
    )

    return driver