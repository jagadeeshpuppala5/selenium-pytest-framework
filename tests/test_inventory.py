import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_add_product_to_cart(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    assert inventory.get_cart_count() == 1


@pytest.mark.xfail(reason="Under Investigation")
def test_remove_product(login):

    inventory = InventoryPage(login)

    inventory.add_product_to_cart()

    assert inventory.get_cart_count() == 1

    inventory.remove_product_from_cart()

    print(
        "Cart Count After Remove:",
        inventory.get_cart_count()
    )

    assert inventory.get_cart_count() == 0
    assert inventory.get_cart_count() == 0