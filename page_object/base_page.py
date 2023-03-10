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
    CART_BNT = (By.CSS_SELECTOR, "#button-cart")
    CART_PRICE = (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")
    CART_MODEL = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")
    CART_DES = (By.CSS_SELECTOR, "#tab-description")
    MAIN_LINKS = (By.ID, "top-links")
    MAIN_LI = (By.TAG_NAME, 'li')
    MAIN_SEARCH = (By.NAME, "search")
    MAIN_MENU = (By.CSS_SELECTOR, "#menu")
    MAIN_FOOTER_B = (By.CSS_SELECTOR, ".col-sm-3")
    MAIN_FOOTER = (By.CSS_SELECTOR, "footer")
