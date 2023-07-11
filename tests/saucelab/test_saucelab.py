import allure
import pytest
from pageObjects.SauceDemo.HomePage import HomePage
from utilities.BaseTest import BaseTest


class TestSauceLab(BaseTest):

    @allure.title("Test End To End")
    @pytest.mark.smoke
    def test_1(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.logIn()
        log.info("Login")
        homePage.addToCart()
        log.info("add to cart")
        checkoutPage = homePage.checkCart()
        checkoutPage.verifyCart()
        log.info("check cart")
        checkoutPage.checkout()
        checkoutPage.verifyCheckoutSuccess()
        log.info("checkout successfully")


