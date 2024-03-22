import pytest


@pytest.mark.main_page
@pytest.mark.usefixtures('login')
class TestMainPageLogin:

    def test_signin(self, app):
        app.main_page.check_is_logged_in()
