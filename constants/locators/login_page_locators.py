from selenium.webdriver.common.by import By

from .general_page_locators import GeneralLocators


class LoginPageLocators(GeneralLocators):
    LOGIN_BTN = (By.CSS_SELECTOR, '.btn-login')
    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, '#loginUserName')
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, '#login-password')
    LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, 'input[type=submit]')
    SOCIAL_MEDIA_BLOCK = (By.CSS_SELECTOR, '.social-login-block')
