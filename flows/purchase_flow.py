# flows/purchase_flow.py

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from data.fake_user import generate_user


class PurchaseFlow:

    def __init__(self, page):
        self.page = page

    def complete_purchase(self, product_slugs: list[str]) -> CheckoutCompletePage:
        """
        Ejecuta el flujo completo de compra:
        - Agrega productos
        - Va al carrito
        - Completa información
        - Finaliza compra
        """

        # Inventory
        inventory = InventoryPage(self.page)
        inventory.add_multiple_products(product_slugs)
        inventory.go_to_cart()

        #  Cart
        cart = CartPage(self.page)
        cart.proceed_to_checkout()

        # Checkout Step One (formulario)
        checkout = CheckoutPage(self.page)
        user = generate_user()

        checkout.fill_information(
            user["first_name"],
            user["last_name"],
            user["postal_code"]
        )

        # Checkout Overview
        overview = CheckoutOverviewPage(self.page)
        overview.finish_purchase()

        # Checkout Complete
        return CheckoutCompletePage(self.page)
