import pytest
from flows.purchase_flow import PurchaseFlow
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.checkout
def test_user_can_complete_purchase(logged_page):

    flow = PurchaseFlow(logged_page)

    complete_page = flow.complete_purchase([
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt"
    ])

    expect(complete_page.complete_header).to_have_text(
        "Thank you for your order!")
