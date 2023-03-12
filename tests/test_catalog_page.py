from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object.catalog_page import CatalogPage


def test_find_element_catalog_page(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    browser.find_element(*CatalogPage.TAG_NAME)
    browser.find_element(*CatalogPage.ADD_CART)
    browser.find_element(*CatalogPage.NAME_CTGR)
    browser.find_element(*CatalogPage.SORT_FILTER)
    browser.find_element(*CatalogPage.A8)


def test_catalog_title(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    assert "Laptops & Notebooks" in browser.title


def test_catalog_cards(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    elements = browser.find_elements(*AdminPage.A8)
    assert len(elements) == 5


def test_add_cart(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    add_to_cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.ADD_CART))
    assert add_to_cart_btn.find_element(*AdminPage.TAG_NAME).text == "ADD TO CART"


def test_category_name(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    name_ctgr = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.NAME_CTGR))
    assert name_ctgr.text == "Laptops & Notebooks"


def test_default_sort_filter(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    sort_filter = browser.find_element(*AdminPage.SORT_FILTER)
    assert "Default" == sort_filter.text
