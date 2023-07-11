import allure
import pytest
from pageObjects.ShopDemo.HomePage import HomePage
from utilities.BaseTest import BaseTest


class TestShopDemoPage(BaseTest):
    @allure.title("End To End Test ShopDemo Page")
    @pytest.mark.regression
    @pytest.mark.parametrize("search_item", ["maxi dress"])
    def test_add_item_to_cart_successfully(self,search_item):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.goToPage()
        log.info("Open Page")
        homePage.search(search_item)
        log.info("search item")
        addToCartPage = homePage.chooseProduct()
        log.info("choose item")
        checkoutPage = addToCartPage.addToCart()
        log.info("add to cart the item")
        homePage.goToCart()
        log.info("check cart")
        checkoutPage.checkout()
        log.info("checkout")
        checkoutPage.verifyCheckoutSuccess()
        log.info("Verify checkout successfully")

    @allure.title("Additional Test ShopDemo Page")
    @pytest.mark.smoke
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
        beforeQuantity = checkoutPage.updateShoppingCartByIncreaseQuantity()
        log.info("update shopping cart")
        checkoutPage.verifyUpdateSuccessByIncreaseQuantity(beforeQuantity)
        log.info("update successfully")


