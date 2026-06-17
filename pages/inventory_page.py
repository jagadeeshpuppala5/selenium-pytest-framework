from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    ADD_TO_CART = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART)

    def remove_product_from_cart(self):

        print("Before Remove Count:", self.get_cart_count())

        self.click(self.REMOVE_BUTTON)

        print("Remove Button Clicked")

        add_buttons = self.driver.find_elements(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )

        print(
            "Add Button Present:",
            len(add_buttons)
        )

    def get_cart_count(self):

        badges = self.driver.find_elements(
            *self.CART_BADGE
        )

        if len(badges) == 0:
            return 0

        return int(badges[0].text)

    def open_cart(self):
        self.click(self.CART_ICON)