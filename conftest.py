# conftest.py

from allure_commons.types import AttachmentType
import allure
import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def logged_page(page):
    page.goto("/")  # usa base_url de pytest.ini

    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_page")

        if page:
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )
