import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.checkout_confirmation import CheckoutConfromation
from utils_common_methods.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shoplink = (By.XPATH, "//li/a[text()='Shop']")
        self.product_card = (By.XPATH,"//div[@class='card h-100']")
        self.CheckOutBtn = (By.XPATH,"//li[@class='nav-item active']/a")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.shoplink ).click()
        products = self.driver.find_elements(*self.product_card)
        print(product_name)
        for product in products:
            ProductName = product.find_element(By.XPATH, "div/h4/a").text
            print(ProductName)
            if ProductName == product_name:
                product.find_element(By.XPATH, "div/button[text()='Add ']").click()
                # self.driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[4]/div/div[2]/button")
                # time.sleep(10)
    def goToCart(self):
        checkoutbtn = self.driver.find_element(*self.CheckOutBtn)
        action = ActionChains(self.driver)
        action.scroll_to_element(checkoutbtn).perform()
        checkoutbtn.click()
        CheckoutConfromationobj = CheckoutConfromation(self.driver)
        return CheckoutConfromationobj





