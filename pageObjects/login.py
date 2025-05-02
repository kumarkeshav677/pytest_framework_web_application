import time
from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage
from utils_common_methods.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signbutton = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signbutton).click()
        ShopPageobj = ShopPage(self.driver)
        time.sleep(5)
        return ShopPageobj
