import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pageObjects.ShopDemo.CheckoutPage import CheckoutPage
from pageObjects.Common.CommonPage import CommonPage


class AddToCartPage(CommonPage):
    colorOption = (By.ID, "pa_color")
    sizeOption = (By.ID, "pa_size")
    addToCartBtn = (By.XPATH, "//button[contains(@class,'add_to_cart')]")
    addToWishList = (By.XPATH, "//div[contains(@class,'summary')]//a[@data-title='Add to Wishlist']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Add product to Cart")
    def addToCart(self):
        self.wait_for_element_appear(AddToCartPage.addToWishList)
        self.wait_for_element_appear(AddToCartPage.colorOption)
        self.wait_for_element_appear(AddToCartPage.sizeOption)
        colorSel = Select(self.driver.find_element(*AddToCartPage.colorOption))
        colorSel.select_by_index(1)
        sizeSel = Select(self.driver.find_element(*AddToCartPage.sizeOption))
        sizeSel.select_by_index(1)
        self.driver.find_element(*AddToCartPage.addToCartBtn).click()
        return CheckoutPage(self.driver)
