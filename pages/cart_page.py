from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    PRODUCT_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    CHECKOUT_BTN = (
        By.ID,
        "checkout"
    )

    CONTINUE_SHOPPING_BTN = (
        By.ID,
        "continue-shopping"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def verify_product_in_cart(self):

        products = self.driver.find_elements(
            *self.PRODUCT_NAME
        )

        return len(products) > 0

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)