import time

import allure
import pytest
from selenium.webdriver.common.by import By
from pageObjects.Common.CommonPage import CommonPage
from pageObjects.UtestSignUp.Step2Page import Step2Page


class Step1Page(CommonPage):
    firstname = (By.ID, "firstName")
    lastname = (By.ID, "lastName")
    email = (By.ID, "email")
    day = (By.ID, "birthDay")
    month = (By.ID, "birthMonth")
    year = (By.ID, "birthYear")
    language = (By.CSS_SELECTOR, "input[type=search]")
    nextBtn = (By.CSS_SELECTOR, "a[role=button]")
    languageChoiceList = (By.XPATH, "//span[contains(@class,'select-choice')]")
    languageChoice = "//*[@placeholder='Add languages']//span[text()='{}']"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open Signup Page")
    def openPage(self):
        self.driver.get("https://www.utest.com/signup/personal")
        self.driver.maximize_window()

    def getFirstName(self):
        return self.driver.find_element(*Step1Page.firstname)

    def getEmail(self):
        return self.driver.find_element(*Step1Page.email)

    def getLastname(self):
        return self.driver.find_element(*Step1Page.lastname)

    def getDay(self):
        return self.driver.find_element(*Step1Page.day)

    def getMonth(self):
        return self.driver.find_element(*Step1Page.month)

    def getYear(self):
        return self.driver.find_element(*Step1Page.year)

    def getLanguage(self):
        return self.driver.find_element(*Step1Page.language)

    def selectLanguage(self, language):
        self.wait_for_element_appear(Step1Page.languageChoiceList)
        languageList = self.driver.find_elements(*Step1Page.languageChoiceList)
        for i in languageList:
            if language.lower() in i.text.lower():
                i.click()
                locator = (By.XPATH, Step1Page.languageChoice.format(language))
                self.wait_for_element_appear(locator)
                break

    def getNextBtn(self):
        return self.driver.find_element(*Step1Page.nextBtn)

    @allure.step("Submit Form with data")
    def submitFormWithData(self, firstName, lastName, email, birthMonth, birthDay, birthYear, language):
        self.wait_for_element_appear(Step1Page.nextBtn)
        self.getFirstName().send_keys(firstName)
        self.getLastname().send_keys(lastName)
        self.getEmail().send_keys(email)
        self.selectOptionByText(self.getYear(), birthYear)
        self.selectOptionByText(self.getMonth(), birthMonth)
        self.selectOptionByText(self.getDay(), birthDay)
        if language is not None:
            self.getLanguage().send_keys(language)
            self.selectLanguage(language)
        time.sleep(1)
        self.getNextBtn().click()
        return Step2Page(self.driver)
