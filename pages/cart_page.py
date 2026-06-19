from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    CHECKOUT_BTN = (
        By.ID,
        "checkout"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_product_name(self):

        return self.driver.find_element(
            *self.CART_ITEM
        ).text

    def verify_product_in_cart(self):

        return (
            self.get_cart_product_name()
            ==
            "Sauce Labs Backpack"
        )

    def click_checkout(self):

        print(
            "Before Checkout Click URL:",
            self.driver.current_url
        )

        self.click(self.CHECKOUT_BTN)

        print(
            "After Checkout Click URL:",
            self.driver.current_url
        )