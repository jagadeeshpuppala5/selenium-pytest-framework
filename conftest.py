import pytest

from pages.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from config.config import BASE_URL
from data.login_data import (
    VALID_USER,
    VALID_PASSWORD
)


@pytest.fixture()
def driver():

    driver = DriverFactory.get_driver()

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