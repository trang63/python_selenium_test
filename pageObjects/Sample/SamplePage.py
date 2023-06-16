from selenium.webdriver.common.by import By

from pageObjects.Sample.ConfirmPage import ConfirmPage


class SamplePage:

    def __init__(self, driver):
        self.driver = driver
    '''
    List all locators here
    '''
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getOneElement(self):
        return self.driver.find_elements(*SamplePage.cardTitle)

    def checkOutItems(self):
        self.driver.find_element(*SamplePage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
