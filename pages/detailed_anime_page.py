from constants.locators.detailed_anime_page_locators import DetailedAnimePageLocators
from .base_page import BasePage


class DetailedAnimePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.__browser = browser

    def check_correct_anime_page_loaded(self, title):
        assert self.get_text(DetailedAnimePageLocators.ANIME_TITLE) == title, 'Provided title is not on the page.'
