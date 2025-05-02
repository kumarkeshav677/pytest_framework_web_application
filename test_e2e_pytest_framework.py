import json

import pytest
from pageObjects.login import LoginPage
test_data_path = "test_data/test_e2e_pytest_framework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_data_item",test_list)
def test_e2e_test(browser_instance, test_data_item):
    driver = browser_instance
    loginpageobj = LoginPage(driver)
    print(loginpageobj.get_title())
    shopPage = loginpageobj.login(test_data_item["userid"], test_data_item["Password"])
    print(shopPage.get_title())
    shopPage.add_product_to_cart(test_data_item["ProductName"])
    CheckoutConfromationobj = shopPage.goToCart()
    CheckoutConfromationobj.checkout()
    CheckoutConfromationobj.enter_delivery_address(test_data_item["Address"])
    CheckoutConfromationobj.validate_order()
