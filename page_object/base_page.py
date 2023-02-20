from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ACCOUNT_LINKS = (By.CSS_SELECTOR, ".list-group")
    NAME_CTGR = (By.CSS_SELECTOR, "#content > h2")
    SORT_FILTER = (By.CSS_SELECTOR, "#input-sort > option[selected]")
    TAG_NAME = (By.TAG_NAME, "span")
    ADD_CART = (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")
    A8 = (By.CSS_SELECTOR, ".product-layout")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[type='submit']")
    A1 = (By.CSS_SELECTOR, "#input-password")
    A2 = (By.CSS_SELECTOR, "fieldset:nth-child(2)")

