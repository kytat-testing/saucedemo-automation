# tests/test_login.py
import pytest
import re
from flows.login_flow import LoginFlow
from data.users import VALID_USER
from playwright.sync_api import expect


@pytest.mark.login
@pytest.mark.positive
@pytest.mark.smoke
def test_successful_login(page):

    flow = LoginFlow(page)
    inventory_page = flow.login_successfully(*VALID_USER)

    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    inventory_page.is_loaded()
    inventory_page.has_correct_title()
