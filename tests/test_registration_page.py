from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object.base_page import AdminPage


def test_find_element_registration_page(browser):
    browser.get(browser.url + "index.php?route=account/register")
    browser.find_element(*AdminPage.A1)
    browser.find_element(*AdminPage.A2)
    browser.find_element(*AdminPage.CONTINUE_BTN)
    browser.find_element(*AdminPage.ACCOUNT_LINKS)


def test_registration_title(browser):
    browser.get(browser.url + "index.php?route=account/register")
    assert "Register Account" in browser.title


def test_continue_btn(browser):
    browser.get(browser.url + "index.php?route=account/register")
    continue_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((AdminPage.CONTINUE_BTN)))
    assert continue_btn.is_enabled()


def test_account_links(browser):
    browser.get(browser.url + "index.php?route=account/register")
    account_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((AdminPage.ACCOUNT_LINKS)))
    assert ("Register" in account_links.text) and ("My Account" in account_links.text)


def test_password_fieldset(browser):
    browser.get(browser.url + "index.php?route=account/register")
    password_fieldset = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((AdminPage.A2)))
    password_fields = password_fieldset.find_elements(*AdminPage.A1)
    for i in password_fields:
        assert i.get_attribute("type") == "password"
