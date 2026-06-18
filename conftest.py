import pytest
from selenium import webdriver
from config.config import BASE_URL
from pages.login_page import LoginPage
from data.login_data import VALID_USER, VALID_PASSWORD


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        VALID_USER,
        VALID_PASSWORD
    )

    yield driver