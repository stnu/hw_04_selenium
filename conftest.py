import pytest
import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests"
    )
    parser.addoption(
        "--driver_storage", default=os.path.expanduser("~/Users/Anna/Desktop/Drivers"),
        help="Browser to run tests"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_storage = request.config.getoption("--driver_storage")

    _driver = None

    if browser_name == "chrom":
        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/chromedriver")
    elif browser_name == "firefox" or browser_name == "ff":
        _driver = webdriver.Firefox(executable_path=f"{driver_storage}/geckodriver")

    yield _driver

    _driver.close()
