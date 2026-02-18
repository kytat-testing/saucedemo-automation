# pages/cart

class CartPage:

 # selectores

    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")

# Acciones

    def proceed_to_checkout(self):
        self.checkout_button.click()
