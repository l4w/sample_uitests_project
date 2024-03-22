from selenium.common.exceptions import NoSuchElementException

from constants import urls
from constants.locators.main_page_locators import MainPageLocators
from constants.locators.top_anime_page_locators import TopAnimePageLocators
from .base_page import BasePage


class TopAnimePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.__browser = browser

    def open_top_anime_page_url(self):
        self.__browser.get(urls.TOP_ANIME_PAGE_URL)

    def top_anime_page_open(self):
        """
        open top anime page from main page 'Anime' dropdown button
        """
        self.click(MainPageLocators.ANIME_DROPDOWN)
        self.click(MainPageLocators.ANIME_DROPDOWN_TOP_ANIME_BTN)
        self.find_element(TopAnimePageLocators.TOP_ANIME_TITLE)

    def get_anime_titles(self) -> tuple:
        """
        returns list of all anime titles on the page

        :return: tuple
        """
        return tuple([element.text for element in self.find_elements(TopAnimePageLocators.TOP_ANIME_TITLE)])

    def check_top_1_anime(self, title: str):
        """
        verify that provided title is top 1 anime in the list

        :param title: name of anime to be checked for being top 1
        """
        self.top_anime_page_open()
        assert self.get_anime_titles()[0] == title, \
            f'Top 1 Anime is not "{title}"'

    def open_anime(self, title: str):
        """
        format a dict with anime-WebElement pairs and clicks on provided anime name

        :param title: name of anime to be opened
        """
        animes = {element.text: element for element in self.find_elements(TopAnimePageLocators.TOP_ANIME_TITLE)}
        if title in animes:
            self.click(animes[title])
        else:
            raise NoSuchElementException(f'there is no "{title}" anime in the list')
