import pytest
from pageObjects.ShopDemo.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomeTask3(BaseClass):

    @pytest.mark.smoke
    def test_add_item_to_cart_successfully(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.goToPage()
        log.info("Open Page")
        homePage.search("mini dress")
        log.info("search item")
        addToCartPage = homePage.chooseProduct()
        log.info("choose item")
        checkoutPage = addToCartPage.addToCart()
        log.info("add to cart the item")
        homePage.goToCart()
        log.info("check cart")
        checkoutPage.checkout()
        log.info("checkout successfully")

    @pytest.mark.random
    def test_add_multiple_item_to_cart_successfully(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.goToPage()
        log.info("Open Page")
        homePage.search("mini dress")
        log.info("search item")
        addToCartPage = homePage.chooseProduct()
        log.info("choose item")
        checkoutPage = addToCartPage.addToCart()
        log.info("add to cart the item")
        homePage.goToCart()
        log.info("check cart")
        checkoutPage.updateShoppingCart()
        log.info("update successfully")


