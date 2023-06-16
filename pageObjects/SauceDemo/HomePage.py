from selenium.webdriver.common.by import By
from pageObjects.SauceDemo.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    loginBtn = (By.ID, "login-button")

    addToCart1Btn = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    cartBadge = (By.XPATH, "//span[@class='shopping_cart_badge']")
    cartBtn = (By.XPATH, "//a[@class='shopping_cart_link']")

    # gender= (By.ID, "exampleFormControlSelect1")
    # submit = (By.XPATH, "//input[@value='Submit']")
    # successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def logIn(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.find_element(*HomePage.username).send_keys("standard_user")
        self.driver.find_element(*HomePage.password).send_keys("secret_sauce")
        self.driver.find_element(*HomePage.loginBtn).click()

    def addToCart(self):
        self.driver.find_element(*HomePage.addToCart1Btn).click()

    def checkCart(self):
        print("Number Of product in cast {}".format(self.driver.find_element(*HomePage.cartBadge).text))
        self.driver.find_element(*HomePage.cartBtn).click()
        assert int(self.driver.find_element(*HomePage.cartBadge).text) == 1
        return CheckoutPage(self.driver)
