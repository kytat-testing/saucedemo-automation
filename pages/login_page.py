# pages/ login

from playwright.sync_api import expect


class LoginPage:

    # selectores
    def __init__(self, page):
        self.page = page
        self.usermame_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')
# Accciones

    def login(self, username, password):
        self.usermame_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def should_show_error(self, expected_text):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)
