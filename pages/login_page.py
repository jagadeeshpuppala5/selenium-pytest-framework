from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger

logger = get_logger()

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        logger.info(f"Entering Username : {username}")

        self.enter_text(self.USERNAME, username)

        logger.info("Entering Password")

        self.enter_text(self.PASSWORD, password)

        logger.info("Clicking Login Button")

        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text