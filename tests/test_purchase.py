import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.regression
@pytest.mark.cart
def test_add_selected_products(logged_page):

    inventory = InventoryPage(logged_page)

    products_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt"
    ]

    inventory.add_multiple_products(products_to_add)

    assert inventory.get_cart_count() == len(products_to_add)
