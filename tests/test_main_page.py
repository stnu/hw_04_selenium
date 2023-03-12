import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object.base_page import AdminPage


def test_find_element_main_page(browser):
    browser.get(browser.url)
    browser.find_element(*AdminPage.MAIN_LINKS)
    browser.find_element(*AdminPage.MAIN_LI)
    browser.find_element(*AdminPage.MAIN_SEARCH)
    browser.find_element(*AdminPage.MAIN_MENU)
    browser.find_element(*AdminPage.MAIN_FOOTER)
    browser.find_element(*AdminPage.MAIN_FOOTER_B)
    time.sleep(2)


def test_main_title(browser):
    browser.get(browser.url)
    assert "Your Store" in browser.title


def test_main_header(browser):
    browser.get(browser.url)
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.MAIN_LINKS))
    elements = header_links.find_elements(*AdminPage.MAIN_LI)
    assert len(elements) == 7


def test_main_search_placeholder(browser):
    browser.get(browser.url)
    search = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.MAIN_SEARCH))
    assert search.get_attribute("placeholder") == "Search"


def test_main_categories_menu(browser):
    browser.get(browser.url)
    menu = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.MAIN_MENU))
    assert "Cameras" in menu.text
    assert "Desktops" in menu.text
    assert "Tablets" in menu.text


def test_footer(browser):
    browser.get(browser.url)
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(AdminPage.MAIN_FOOTER))
    elements = header_links.find_elements(*AdminPage.MAIN_FOOTER_B)
    assert len(elements) == 4
