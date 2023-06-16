from selenium.webdriver.common.by import By
from pageObjects.ShopDemo.CommonPage import CommonPage as Page


class CheckoutPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    checkoutBtn = (By.XPATH, "//a[contains(text(),'Proceed to checkout')]")
    placeOrderBtn = (By.ID, "place_order")
    plusIcon = (By.XPATH, "(//i[@class='icon_plus'])[1]")
    itemPrice = (By.XPATH, "(//td[@class='product-price']//bdi)[1]")
    itemQuantity = (By.XPATH, "(//td[@class='product-quantity']//input[contains(@id,'quantity')])[1]")
    totalItemPrice = (By.XPATH, "(//td[@class='product-subtotal']//bdi)[1]")
    updateCartBtn = (By.XPATH, "//input[@name='update_cart']")

    def checkCartItems(self):
        pass

    def checkout(self):
        self.wait_for_element_appear(CheckoutPage.checkoutBtn)
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        self.wait_for_element_appear(CheckoutPage.placeOrderBtn)

    def updateShoppingCart(self):
        log = self.getLogger()
        self.wait_for_element_appear(CheckoutPage.checkoutBtn)
        log.info(
            "--------- quantity is " + self.driver.find_element(*CheckoutPage.itemQuantity).get_attribute("value"))
        beforeQuantity = int(self.driver.find_element(*CheckoutPage.itemQuantity).get_attribute("value"))
        self.driver.find_element(*CheckoutPage.plusIcon).click()
        self.driver.find_element(*CheckoutPage.updateCartBtn).click()
        afterQuantity = int(self.driver.find_element(*CheckoutPage.itemQuantity).get_attribute("value"))
        assert beforeQuantity + 1 == afterQuantity, "{} and {}".format(beforeQuantity, afterQuantity)
        price = float(self.driver.find_element(*CheckoutPage.itemPrice).text[1:])
        totalPrice = float(self.driver.find_element(*CheckoutPage.totalItemPrice).text[1:])
        assert totalPrice == price * afterQuantity, "Price is {} and quantity is {} and total is {}".format(price,afterQuantity,totalPrice)
