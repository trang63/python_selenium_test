from pageObjects.Common.CommonPage import CommonPage
from selenium.webdriver.common.by import By
import allure


class CheckoutPage(CommonPage):
    checkoutBtn = (By.XPATH, "//button[@data-test='checkout']")
    firstname = (By.XPATH, "//input[@data-test='firstName']")
    lastname = (By.XPATH, "//input[@data-test='lastName']")
    code = (By.XPATH, "//input[@data-test='postalCode']")
    continueBtn = (By.XPATH, "//input[@data-test='continue']")
    finishBtn = (By.XPATH, "//button[@data-test='finish']")
    completeMsg = (By.XPATH, "//*[@class='title']")

    productName = 'Sauce Labs Backpack'
    price = '$29.99'
    cartProductName = (By.CSS_SELECTOR, '.inventory_item_name')
    cartProductPrice = (By.CSS_SELECTOR, '.inventory_item_price')
    cartBadge = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        self.driver = driver

    def checkCartItems(self):
        pass

    def verifyCart(self):
        self.wait_for_element_appear(CheckoutPage.checkoutBtn)
        assert int(self.driver.find_element(*CheckoutPage.cartBadge).text) == 1
        assert self.driver.find_element(*CheckoutPage.cartProductName).text == CheckoutPage.productName
        assert self.driver.find_element(*CheckoutPage.cartProductPrice).text == CheckoutPage.price

    @allure.step("Finish Checkout")
    def checkout(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        self.wait_for_element_appear(CheckoutPage.continueBtn)
        self.driver.find_element(*CheckoutPage.firstname).send_keys("abc")
        self.driver.find_element(*CheckoutPage.lastname).send_keys("def")
        self.driver.find_element(*CheckoutPage.code).send_keys("70000")
        self.driver.find_element(*CheckoutPage.continueBtn).click()
        self.driver.implicitly_wait(10)
        self.wait_for_element_appear(CheckoutPage.finishBtn)
        self.driver.find_element(*CheckoutPage.finishBtn).click()

    def verifyCheckoutSuccess(self):
        assert str(self.driver.find_element(*CheckoutPage.completeMsg).text) == "Checkout: Complete!..."
