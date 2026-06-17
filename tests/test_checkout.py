import pytest

from data.login_data import (
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE
)

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.regression
def test_complete_checkout(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    assert inventory.get_cart_count() == 1

    inventory.open_cart()

    cart_page = CartPage(login)

    assert cart_page.verify_product_in_cart()

    cart_page.click_checkout()

    checkout = CheckoutPage(login)

    checkout.enter_checkout_details(
        FIRST_NAME,
        LAST_NAME,
        POSTAL_CODE
    )

    checkout.click_continue()

    checkout.click_finish()

    assert (
        checkout.get_success_message()
        ==
        "Thank you for your order!"
    )