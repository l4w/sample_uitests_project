from .base_page import BasePage
from constants.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.__browser = browser

    def check_is_logged_in(self):
        self.find_element(MainPageLocators.LOGGED_STATS_PANEL)
