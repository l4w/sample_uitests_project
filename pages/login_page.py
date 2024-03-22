from pages.base_page import BasePage
from constants.locators.login_page_locators import LoginPageLocators
from constants import credentials


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.__browser = browser

    def check_login_page_loaded(self):
        self.find_element(LoginPageLocators.SOCIAL_MEDIA_BLOCK)

    def open_login_page(self):
        self.click(LoginPageLocators.LOGIN_BTN)
        self.check_login_page_loaded()

    def login(self):
        self.open_login_page()
        self.send_keys(LoginPageLocators.LOGIN_USERNAME_FIELD, credentials.USERNAME)
        self.send_keys(LoginPageLocators.LOGIN_PASSWORD_FIELD, credentials.PASSWORD)
        self.click(LoginPageLocators.LOGIN_SUBMIT_BTN)
