import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.browserutils import BrowserUtils


class CheckoutConfromation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.successchecoutbtn = (By.XPATH,"//button[@class='btn btn-success']")
        self.selct_country_inputbox = (By.XPATH,"//input[@id='country']")
        self.purches_btn = (By.XPATH,"//input[@value='Purchase']")
        self.successmesssage = (By.XPATH, "//div/strong[text()='Success!']")
        self.country_option = (By.XPATH,"//li/a[text()='India']")

    def checkout(self):
        self.driver.find_element(*self.successchecoutbtn).click()


    def enter_delivery_address(self, CountryName):
        self.driver.find_element(*self.selct_country_inputbox).send_keys(CountryName)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located(self.country_option)).click()
        self.driver.find_element(*self.purches_btn).click()

    def validate_order(self):
        message = self.driver.find_element(*self.successmesssage).text
        print(message)
        assert "Success!" in message


