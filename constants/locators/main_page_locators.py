from selenium.webdriver.common.by import By

from .general_page_locators import GeneralLocators


class MainPageLocators(GeneralLocators):
    ANIME_DROPDOWN = (By.XPATH, '//ul[@id="nav"]/li/a[text()="Anime"]')
    ANIME_DROPDOWN_TOP_ANIME_BTN = (
        By.XPATH, '//ul[@id="nav"]/li/a[text()="Anime"]/following-sibling::ul/li/a[text()="Top Anime"]')

    LOGGED_STATS_PANEL = (By.CSS_SELECTOR, '.my_statistics')
