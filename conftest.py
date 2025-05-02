import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service = service_obj)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service = service_obj)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        driver.maximize_window()

    yield driver
    # driver.close()




