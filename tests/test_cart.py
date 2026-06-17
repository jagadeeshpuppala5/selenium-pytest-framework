import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_verify_product_in_cart(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    inventory.open_cart()

    cart_page = CartPage(login)

    assert cart_page.verify_product_in_cart()


@pytest.mark.regression
def test_checkout_button(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    inventory.open_cart()

    print("Current URL:", login.current_url)

    cart_page = CartPage(login)

    cart_page.click_checkout()

    assert "checkout-step-one" in login.current_url