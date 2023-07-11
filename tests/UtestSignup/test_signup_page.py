import allure
import pytest
from utilities.BaseTest import BaseTest
from pageObjects.UtestSignUp.Step1Page import Step1Page


class TestUtestPage(BaseTest):
    @allure.title("Test Signup Page")
    @pytest.mark.usefixtures("getData")
    def test_SignUp(self, getData):
        log = self.getLogger()
        firstName = getData["firstname"]
        lastName = getData["lastname"]
        email = getData["email"]
        birthDay = getData["birthDay"]
        birthMonth = getData["birthMonth"]
        birthYear = getData["birthYear"]
        language = getData["language"]
        step1Page = Step1Page(self.driver)
        step1Page.openPage()
        log.info("Submit form with data")
        step2Page = step1Page.submitFormWithData(firstName, lastName, email, birthMonth, birthDay, birthYear, language)
        step2Page.verifyAtStep2()
