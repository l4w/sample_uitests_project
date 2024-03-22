from selenium.webdriver.common.by import By

from .general_page_locators import GeneralLocators


class DetailedAnimePageLocators(GeneralLocators):
    ANIME_TITLE = (By.CSS_SELECTOR, 'h1[class="title-name h1_bold_none"] > strong')
