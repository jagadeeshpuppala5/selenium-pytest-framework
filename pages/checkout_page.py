from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger

logger = get_logger()


class CheckoutPage(BasePage):

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BTN = (
        By.ID,
        "continue"
    )

    FINISH_BTN = (
        By.ID,
        "finish"
    )

    SUCCESS_MSG = (
        By.CLASS_NAME,
        "complete-header"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def enter_checkout_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        logger.info("Entering checkout details")

        self.enter_text(
            self.FIRST_NAME,
            first_name
        )

        self.enter_text(
            self.LAST_NAME,
            last_name
        )

        self.enter_text(
            self.POSTAL_CODE,
            postal_code
        )

    def click_continue(self):

        logger.info("Clicking Continue Button")

        self.click(self.CONTINUE_BTN)

    def click_finish(self):

        logger.info("Clicking Finish Button")

        self.click(self.FINISH_BTN)

    def get_success_message(self):

        return self.get_text(
            self.SUCCESS_MSG
        )