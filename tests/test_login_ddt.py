import pytest

from pages.login_page import LoginPage
from config.config import BASE_URL
from data.login_test_data import LOGIN_TEST_DATA


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected",
    LOGIN_TEST_DATA
)
def test_login_ddt(
        driver,
        username,
        password,
        expected
):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        username,
        password
    )

    if expected:

        assert "inventory" in driver.current_url

    else:

        assert (
            "Epic sadface"
            in
            login_page.get_error_message()
        )