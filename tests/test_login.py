from data.login_data import *
from config.config import BASE_URL
from pages.login_page import LoginPage
from utilities.logger import get_logger
import pytest

logger = get_logger()


@pytest.mark.smoke
def test_valid_login(driver):

    logger.info("Starting Valid Login Test")

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    logger.info("Entering valid credentials")

    login_page.login(
        VALID_USER,
        VALID_PASSWORD
    )

    logger.info("Verifying successful login")

    assert "inventory" in driver.current_url

    logger.info("Valid Login Test Passed")


@pytest.mark.regression
def test_invalid_login(driver):

    logger.info("Starting Invalid Login Test")

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    logger.info("Entering invalid credentials")

    login_page.login(
        INVALID_USER,
        INVALID_PASSWORD
    )

    logger.info("Verifying error message")

    assert "Username and password do not match" in login_page.get_error_message()

    logger.info("Invalid Login Test Passed")


@pytest.mark.regression
def test_blank_username(driver):

    logger.info("Starting Blank Username Test")

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        "",
        VALID_PASSWORD
    )

    logger.info("Verifying username required error")

    assert "Username is required" in login_page.get_error_message()

    logger.info("Blank Username Test Passed")


@pytest.mark.regression
def test_blank_password(driver):

    logger.info("Starting Blank Password Test")

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        VALID_USER,
        ""
    )

    logger.info("Verifying password required error")

    assert "Password is required" in login_page.get_error_message()

    logger.info("Blank Password Test Passed")