# flows/login_flow.py

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class LoginFlow:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.goto("/")
        login_page = LoginPage(self.page)
        login_page.login(username, password)
        return login_page

    def login_successfully(self, username, password):
        self.page.goto("/")
        login_page = LoginPage(self.page)
        login_page.login(username, password)
        return InventoryPage(self.page)
