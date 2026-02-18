class CheckoutCompletePage:

    def __init__(self, page):
        self.page = page
        self.complete_header = page.locator(".complete-header")
