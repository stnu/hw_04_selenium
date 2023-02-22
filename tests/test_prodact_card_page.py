import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object.base_page import AdminPage


def test_find_element_cart_page(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=44")
    browser.find_element(*AdminPage.CART_BNT)
    browser.find_element(*AdminPage.CART_PRICE)
    browser.find_element(*AdminPage.CART_MODEL)
    browser.find_element(*AdminPage.CART_DES)
    time.sleep(2)


def test_product_title(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=44")
    assert "MacBook Air" in browser.title


def test_product_title_model(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=44")
    product_title = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.CART_MODEL))
    assert product_title.text == "MacBook Air"


def test_product_button(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=44")
    cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.CART_BNT))
    assert cart_btn.is_enabled()


def test_product_price(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=44")
    product_price = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.CART_PRICE))
    assert product_price.text == "$1,202.00"


def test_product_description(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=44")
    product_description = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.CART_DES))
    assert "MacBook Air" in product_description.text
