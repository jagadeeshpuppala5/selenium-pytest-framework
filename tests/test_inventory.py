import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_add_product_to_cart(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    assert inventory.get_cart_count() == 1

@pytest.mark.regression
def test_remove_product(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    assert inventory.get_cart_count() == 1

    inventory.remove_product_from_cart()

    assert inventory.get_cart_count() == 0