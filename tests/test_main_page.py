import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object.main_page import MainPage


def test_find_element_main_page(browser):
    browser.get(browser.url)
    browser.find_element(*MainPage.MAIN_LINKS)
    browser.find_element(*MainPage.MAIN_LI)
    browser.find_element(*MainPage.MAIN_SEARCH)
    browser.find_element(*MainPage.MAIN_MENU)
    browser.find_element(*MainPage.MAIN_FOOTER)
    browser.find_element(*MainPage.MAIN_FOOTER_B)
    time.sleep(2)


def test_main_title(browser):
    browser.get(browser.url)
    assert "Your Store" in browser.title


def test_main_header(browser):
    browser.get(browser.url)
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.MAIN_LINKS))
    elements = header_links.find_elements(*MainPage.MAIN_LI)
    assert len(elements) == 7


def test_main_search_placeholder(browser):
    browser.get(browser.url)
    search = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.MAIN_SEARCH))
    assert search.get_attribute("placeholder") == "Search"


def test_main_categories_menu(browser):
    browser.get(browser.url)
    menu = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.MAIN_MENU))
    assert "Cameras" in menu.text
    assert "Desktops" in menu.text
    assert "Tablets" in menu.text


def test_footer(browser):
    browser.get(browser.url)
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.MAIN_FOOTER))
    elements = header_links.find_elements(*MainPage.MAIN_FOOTER_B)
    assert len(elements) == 4
