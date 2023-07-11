import allure
from selenium.webdriver.common.by import By
from pageObjects.Common.CommonPage import CommonPage


class Step2Page(CommonPage):
    city = (By.ID, "city")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Submit Form with data")
    def verifyAtStep2(self):
        self.wait_for_element_appear(Step2Page.city)
        assert self.get_current_url() == 'https://www.utest.com/signup/address'






