from pages.detailed_anime_page import DetailedAnimePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.top_anime_page import TopAnimePage


class Application:

    def __init__(self, browser):
        self.main_page = MainPage(browser)
        self.login_page = LoginPage(browser)
        self.top_anime_page = TopAnimePage(browser)
        self.detailed_anime_page = DetailedAnimePage(browser)
