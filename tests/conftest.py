import pytest
from selenium import webdriver

# selenium 4.* chrome webdriver handling
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from scripts.app import Application
from constants import urls


def pytest_addoption(parser):
    parser.addoption(
        '--headless', action='store', default='on', help='used to turn on/off headless mode for tests'
    )


@pytest.fixture(scope='session', autouse=True)
def headless(request):
    return request.config.getoption('--headless')


@pytest.fixture(scope='class')
def browser(headless):
    options = webdriver.ChromeOptions()
    if headless == 'on':
        options.add_argument('headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-extensions')
    options.add_argument('--ignore-certificate-errors')
    # to remove unknown logs from chromedriver "DevTools listening on ws:"
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # selenium 4.* chrome webdriver handling: service=Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    browser.get(urls.MAIN_PAGE_URL)
    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def app(browser):
    return Application(browser)


@pytest.fixture(scope='class')
def login(app):
    app.login_page.login()
    app.main_page.check_is_logged_in()
