# pages/finish processing

class CheckoutOverviewPage:

 # selectores

    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator("#finish")

 # Acciones

    def finish_purchase(self):
        self.finish_button.click()
