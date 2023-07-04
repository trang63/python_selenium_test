from pageObjects.Common.CommonPage import CommonPage
from selenium.webdriver.common.by import By
from pageObjects.SauceDemo.CheckoutPage import CheckoutPage
import allure
import pytest


class HomePage(CommonPage):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    loginBtn = (By.ID, "login-button")

    addToCartBtn = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")

    cartBadge = (By.XPATH, "//span[@class='shopping_cart_badge']")
    cartBtn = (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def logIn(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.find_element(*HomePage.username).send_keys("standard_user")
        self.driver.find_element(*HomePage.password).send_keys("secret_sauce")
        self.driver.find_element(*HomePage.loginBtn).click()

    @allure.step("Add item to Cart")
    def addToCart(self):
        self.driver.find_element(*HomePage.addToCartBtn).click()

    @allure.step("Checkout product")
    def checkCart(self):
        print("Number Of product in cast {}".format(self.driver.find_element(*HomePage.cartBadge).text))
        self.driver.find_element(*HomePage.cartBtn).click()
        return CheckoutPage(self.driver)
