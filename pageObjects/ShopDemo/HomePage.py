import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.ShopDemo.CheckoutPage import CheckoutPage
from pageObjects.ShopDemo.AddToCartPage import AddToCartPage
from pageObjects.Common.CommonPage import CommonPage


class HomePage(CommonPage):
    searchIcon = (By.XPATH, "//a[@class='noo-search']")
    searchInput = (By.XPATH, "//input[@name='s']")
    productTitleList = (By.XPATH, "//div[contains(@class,'product-inner')]//h3/a")
    productFirst = (By.XPATH, "(//div[contains(@class,'product-inner')]//h3/a)[1]")
    addedMessage = (By.XPATH,"//div[contains(@class,'notices') and contains(normalize-space(),'been added to your cart')]")
    cartInfo = (By.XPATH, "//span[@class='cart-name-and-total']")
    cartIcon = (By.XPATH, "//i[@class='icon_bag_alt']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open webpage")
    def goToPage(self):
        self.driver.get("https://shop.demoqa.com/")
        self.driver.maximize_window()

    @allure.step("Search product {search_str}")
    def search(self, search_str):
        self.driver.find_element(*HomePage.searchIcon).click()
        self.wait_for_element_appear(HomePage.searchInput)
        self.driver.find_element(*HomePage.searchInput).send_keys(search_str)
        self.driver.find_element(*HomePage.searchInput).send_keys(Keys.RETURN)

    @allure.step("Choose a product")
    def chooseProduct(self):
        self.driver.implicitly_wait(2000)
        self.wait_for_element_appear(HomePage.productFirst)
        self.driver.find_element(*HomePage.productFirst).click()
        return AddToCartPage(self.driver)

    @allure.step("Go to cart")
    def goToCart(self):
        self.wait_for_element_appear(HomePage.addedMessage)
        self.wait_for_element_appear(HomePage.cartIcon)
        self.driver.find_element(*HomePage.cartIcon).click()
        return CheckoutPage(self.driver)
