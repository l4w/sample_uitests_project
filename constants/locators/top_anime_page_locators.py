from selenium.webdriver.common.by import By

from .general_page_locators import GeneralLocators


class TopAnimePageLocators(GeneralLocators):
    PAGE = (By.XPATH, '//div[@id="myanimelist"]')
    TOP_ANIME_TITLE = (By.XPATH, f'{PAGE[1]}//table[@class="top-ranking-table"]//div[@class="di-ib clearfix"]')
    ADD_TO_LIST_BTN = (By.XPATH, f'{PAGE[1]}//a[text()="Add to list"]')
    WATCHING_BTN = (By.XPATH, f'{PAGE[1]}//a[text()="Watching"]')
    h1 = (By.CSS_SELECTOR, '.h1')

    class AnimeIFrame:
        IFRAME = (By.CSS_SELECTOR, '#fancybox-frame')
        SUBMIT_BTN = (By.XPATH, '//td/div/input[@class="inputButton main_submit"]')
        SUCCESSFULLY_ADDED_TEXT = (By.XPATH, '//*[text()="Successfully added anime to your list."]')
        DELETE_BTN = (By.XPATH, '//td/div/form/input[@class="inputButton ml8 delete_submit"]')
        SUCCESSFULLY_DELETED_TEXT = (By.XPATH, '//*[text()="Successfully deleted entry."]')
