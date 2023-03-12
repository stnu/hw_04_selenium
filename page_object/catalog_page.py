from selenium.webdriver.common.by import By


class CatalogPage:
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    NAME_CTGR = (By.CSS_SELECTOR, "#content > h2")
    SORT_FILTER = (By.CSS_SELECTOR, "#input-sort > option[selected]")
    TAG_NAME = (By.TAG_NAME, "span")
    A8 = (By.CSS_SELECTOR, ".product-layout")
    ADD_CART = (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")