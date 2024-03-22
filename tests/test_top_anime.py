import pytest
from constants.locators.top_anime_page_locators import TopAnimePageLocators


@pytest.mark.top_anime_page
@pytest.mark.usefixtures('login')
class TestTopAnimePage:

    def test_alchemist_is_top_1_anime(self, app):
        app.top_anime_page.check_top_1_anime('Fullmetal Alchemist: Brotherhood')

    def test_add_anime_to_list_from_top_anime_page(self, app):
        app.top_anime_page.open_top_anime_page_url()
        app.top_anime_page.click(TopAnimePageLocators.ADD_TO_LIST_BTN)
        app.top_anime_page.switch_to(TopAnimePageLocators.AnimeIFrame.IFRAME)
        app.top_anime_page.click(TopAnimePageLocators.AnimeIFrame.SUBMIT_BTN)
        app.top_anime_page.find_element(TopAnimePageLocators.AnimeIFrame.SUCCESSFULLY_ADDED_TEXT)

    def test_open_anime_from_top_page(self, app):
        title = 'Fullmetal Alchemist: Brotherhood'
        app.top_anime_page.open_top_anime_page_url()
        app.top_anime_page.open_anime(title)
        app.detailed_anime_page.check_correct_anime_page_loaded(title)

    def test_delete_anime_from_top_page(self, app):
        app.top_anime_page.open_top_anime_page_url()
        app.top_anime_page.click(TopAnimePageLocators.WATCHING_BTN)
        app.top_anime_page.switch_to(TopAnimePageLocators.AnimeIFrame.IFRAME)
        app.top_anime_page.click(TopAnimePageLocators.AnimeIFrame.DELETE_BTN)
        app.top_anime_page.switch_to('alert').accept()
        app.top_anime_page.find_element(TopAnimePageLocators.AnimeIFrame.SUCCESSFULLY_DELETED_TEXT)
