from selenium.webdriver.common.by import By


class ProductPage:

    CART_BNT = (By.CSS_SELECTOR, "#button-cart")
    CART_PRICE = (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")
    CART_MODEL = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")
    CART_DES = (By.CSS_SELECTOR, "#tab-description")