# test_login_with_locked_user
# test_login_invalid_credentials
# test_login_with_empty_fields

import pytest
from flows.login_flow import LoginFlow
from data.users import LOCKED_USER, INVALID_USER, EMPTY_USER
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize(
    "user, expected_error",
    [
        (LOCKED_USER, "locked out"),
        (INVALID_USER, "Username and password"),
        (EMPTY_USER, "Username is required"),
    ],
)
def test_login_negative_scenarios(page, user, expected_error):

    flow = LoginFlow(page)
    login_page = flow.login(*user)

    login_page.should_show_error(expected_error)
