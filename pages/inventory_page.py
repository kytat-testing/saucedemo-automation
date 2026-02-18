# pages/inventory
from playwright.sync_api import expect


class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.shopping_cart = page.locator("#shopping_cart_container")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.title = page.locator(".title")

    def is_loaded(self):
        expect(self.shopping_cart).to_be_visible()

    def has_correct_title(self):
        expect(self.title).to_have_text("Products")

    def add_multiple_products(self, product_slugs):
        for slug in product_slugs:
            self.page.locator(f"#add-to-cart-{slug}").click()

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def go_to_cart(self):
        self.shopping_cart.click()
