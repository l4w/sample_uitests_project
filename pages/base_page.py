from typing import Union, Optional

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from scripts.singleton import Singleton
from scripts.logger import logger


class BasePage(Singleton):
    __TIMEOUT = 10
    __INTERVAL = 0.5

    def __init__(self, browser):
        self.__browser = browser

    def wait(self, timeout: float = __TIMEOUT, interval: float = __INTERVAL):
        return WebDriverWait(self.__browser, timeout, interval)

    def find_element(self,
                     unit: Union[tuple, WebElement],
                     timeout: float = __TIMEOUT,
                     interval: float = __INTERVAL,
                     safe: bool = False) -> Optional[WebElement]:
        """
        waits for element to be visible

        :param unit: element locator
        :param timeout: wait time in seconds till element is visible
        :param interval: time in seconds between polls
        :param safe: if True - do not throw exception in case if element is not visible
        :return: WebElement
        """
        if isinstance(unit, tuple):
            try:
                return self.wait(timeout, interval).until(EC.visibility_of_element_located(unit))
            except TimeoutException:
                if safe:
                    return
                raise TimeoutException(f'element {unit[1]} is not visible')
        else:
            return unit

    def click(self,
              unit: Union[tuple, WebElement],
              timeout: float = __TIMEOUT,
              interval: float = __INTERVAL,
              safe: bool = False) -> bool:
        """
        find an element and click on it

        :param unit: element locator or WebElement
        :param timeout: wait time in seconds till element is visible
        :param interval: time in seconds between polls
        :param safe: if True - do not throw exception in case if element is not visible
        :return: bool
        """
        element = self.find_element(unit, timeout, interval, safe)
        logger.info(f'element: {element}')
        if element is not None:
            assert element.is_enabled()
            element.click()
            logger.info(f'click: {unit} element was clicked.')
            return True
        return False

    def find_elements(self,
                      units: tuple,
                      timeout: float = __TIMEOUT,
                      interval: float = __INTERVAL,
                      safe: bool = False) -> Union[WebElement, None, tuple]:
        """
        waits for elements to be visible

        :param units: element locator
        :param timeout: wait time in seconds till element is visible
        :param interval: time in seconds between polls
        :param safe: if True - do not throw exception in case if element is not visible
        :return: WebElement
        """
        try:
            return self.wait(timeout, interval).until(EC.visibility_of_all_elements_located(units))
        except TimeoutException:
            if safe:
                return
            raise TimeoutException(f'element {units[1]} is not visible')

    def send_keys(self,
                  unit: Union[tuple, WebElement],
                  text: str,
                  timeout: float = __TIMEOUT,
                  interval: float = __INTERVAL,
                  safe: bool = False) -> bool:
        """
        find an element and set text to it

        :param unit: element locator or WebElement
        :param text: string to be passed to element
        :param timeout: wait time in seconds till element is visible
        :param interval: time in seconds between polls
        :param safe: if True - do not throw exception in case if element is not visible
        :return: bool
        """
        element = self.find_element(unit, timeout, interval, safe)
        if element is not None:
            assert element.is_enabled()
            element.send_keys(text)
            logger.info(f'send_keys: {text} was passed into {unit}')
            return True
        return False

    def __switch_to(self,
                    unit: Union[tuple, WebElement],
                    safe: bool = False) -> bool:
        """
        find an element and switch to it

        :param unit: element locator or WebElement or str to be switched to alert
        :param safe: if True - do not throw exception in case if element is not visible
        :return: bool or Alert
        """
        element = self.find_element(unit, 0, 0, safe)
        if element is not None:
            self.__browser.switch_to.frame(element)
            return True
        return False

    def switch_to(self,
                  unit: Union[tuple, WebElement, str],
                  safe: bool = False) -> Union[Alert, bool]:
        """
        wait till self.__switch_to method is executed
        if 'alert' string is passed, switch to alert

        :param unit: element locator or WebElement or str to be switched to alert
        :param safe: if True - do not throw exception in case if element is not visible
        :return: bool or Alert
        """
        if unit == 'alert':
            self.wait().until(EC.alert_is_present())
            return self.__browser.switch_to.alert
        else:
            return self.wait().until(lambda d: self.__switch_to(unit, safe))

    def get_text(self,
                 unit: Union[tuple, WebElement],
                 timeout: float = __TIMEOUT,
                 interval: float = __INTERVAL,
                 safe: bool = False) -> Union[str, bool]:
        """
        find element and return its text

        :param unit: element locator
        :param timeout: wait time in seconds till element is visible
        :param interval: time in seconds between polls
        :param safe: if True - do not throw exception in case if element is not visible
        :return: element.text if element is found else - False (if safe is True)
        """
        element = self.find_element(unit, timeout, interval, safe)
        if element is not None:
            return element.text
        return False
