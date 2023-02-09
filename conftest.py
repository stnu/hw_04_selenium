import pytest
from selenium import webdriver

DRIVERS_STORAGE = "/Users/Anna/Desktop/Drivers/chromedriver.exe"


@pytest.fixture()
def driver():
    return webdriver.Chrome(executable_path=f"{DRIVERS_STORAGE}/chromedriver")
