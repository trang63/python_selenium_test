from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pageObjects.SauceDemo.CommonPage import CommonPage as Page


class CheckoutPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    checkoutBtn = (By.XPATH, "//button[@data-test='checkout']")
    firstname = (By.XPATH, "//input[@data-test='firstName']")
    lastname = (By.XPATH, "//input[@data-test='lastName']")
    code = (By.XPATH, "//input[@data-test='postalCode']")
    continueBtn = (By.XPATH, "//input[@data-test='continue']")
    finishBtn = (By.XPATH, "//button[@data-test='finish']")
    completeMsg = (By.XPATH, "//*[@class='title']")

    # gender= (By.ID, "exampleFormControlSelect1")
    # submit = (By.XPATH, "//input[@value='Submit']")
    # successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def checkCartItems(self):
        pass

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
        assert str(self.driver.find_element(*CheckoutPage.completeMsg).text) == "Checkout: Complete!"
