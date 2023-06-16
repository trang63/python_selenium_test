import inspect

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.ShopDemo.CheckoutPage import CheckoutPage
from pageObjects.ShopDemo.CommonPage import CommonPage as Page
from pageObjects.ShopDemo.AddToCartPage import AddToCartPage

import logging
import logging.config

# Load the logging configuration from the file
logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger("mylogger")
logger.propagate = False


class HomePage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    searchIcon = (By.XPATH, "//a[@class='noo-search']")
    searchInput = (By.XPATH, "//input[@name='s']")
    productTitleList = (By.XPATH, "//div[contains(@class,'product-inner')]//h3/a")
    productFirst = (By.XPATH, "(//div[contains(@class,'product-inner')]//h3/a)[1]")

    cartInfo = (By.XPATH, "//span[@class='cart-name-and-total']")
    cartIcon = (By.XPATH, "//i[@class='icon_bag_alt']")

    def goToPage(self):
        self.driver.get("https://shop.demoqa.com/")
        self.driver.maximize_window()
        logger.info("This is an info log message")

    def search(self, search_str):
        self.driver.find_element(*HomePage.searchIcon).click()
        self.wait_for_element_appear(HomePage.searchInput)
        self.driver.find_element(*HomePage.searchInput).send_keys(search_str)
        self.driver.find_element(*HomePage.searchInput).send_keys(Keys.RETURN)

    def chooseProduct(self):
        # self.driver.find_elements(*HomePage.productTitleList)[0].click()
        self.driver.implicitly_wait(2000)
        self.wait_for_element_appear(HomePage.productFirst)
        self.driver.find_element(*HomePage.productFirst).click()
        return AddToCartPage(self.driver)

    def goToCart(self):
        self.driver.find_element(*HomePage.cartIcon).click()
        return CheckoutPage(self.driver)
