import pytest
import os
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests")
    parser.addoption("--url", default="http://192.168.56.1:8081/")
    parser.addoption("--drivers", default=os.path.expanduser("~/Users/Anna/Desktop/Drivers"),
                     help="Browser to run tests")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox" or "ff":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError("Browser not supported!")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
