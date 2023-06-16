import pytest
from pageObjects.SauceDemo.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomeTask(BaseClass):

    @pytest.mark.smoke
    def test_home_2(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.logIn()
        log.info("Login")
        homePage.addToCart()
        log.info("add to cart")
        checkoutPage = homePage.checkCart()
        log.info("check cart")
        checkoutPage.checkout()
        log.info("checkout successfully")


