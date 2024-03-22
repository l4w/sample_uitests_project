import pytest


@pytest.mark.login_page
class TestLoginPage:

    def test_open_login_page(self, app):
        app.login_page.open_login_page()
