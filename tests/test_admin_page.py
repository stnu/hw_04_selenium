import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object.base_page import AdminPage


def test_page_title(browser):
    browser.get(browser.url + "/admin")
    assert "Administration" in browser.title


def test_find_element_login_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*AdminPage.USERNAME_INPUT)
    browser.find_element(*AdminPage.PASSWORD_INPUT)
    browser.find_element(*AdminPage.SUBMIT_BUTTON)
    browser.find_element(*AdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*AdminPage.OPENCART_LINK)
    time.sleep(2)


def test_username_field(browser):
    browser.get(browser.url + "/admin")
    username_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((AdminPage.USERNAME_INPUT)))
    assert username_field.get_attribute("placeholder") == "Username"


def test_password_field(browser):
    browser.get(browser.url + "/admin")
    password_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((AdminPage.PASSWORD_INPUT)))
    assert password_field.get_attribute("placeholder") == "Password"


def test_login_btn(browser):
    browser.get(browser.url + "/admin")
    login_btn = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (AdminPage.LOGIN_BTN)))
    assert login_btn.text == "Login"
    assert login_btn.is_enabled()


def test_forgotten_pswrd(browser):
    browser.get(browser.url + "/admin")
    forgotten_pswrd = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (AdminPage.FORGOTTEN_PASSWORD)))
    assert forgotten_pswrd.text == "Forgotten Password"
