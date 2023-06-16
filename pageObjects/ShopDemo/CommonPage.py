import inspect

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
import logging.config


class CommonPage:

    # Load the logging configuration from the file
    logging.config.fileConfig('logging_config.ini')
    log = logging.getLogger("mylogger")

    def __init__(self, driver):
        self.driver = driver

    def getLogger(self):
        return self.log

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def wait_for_element_appear(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with locator '{locator}' did not  appear within the given timeout.")

    def wait_for_element_disappear(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with locator '{locator}' did not  disappear within the given timeout.")

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
