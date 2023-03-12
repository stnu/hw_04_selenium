from selenium.webdriver.common.by import By


class MainPage:
    MAIN_LINKS = (By.ID, "top-links")
    MAIN_LI = (By.TAG_NAME, 'li')
    MAIN_SEARCH = (By.NAME, "search")
    MAIN_MENU = (By.CSS_SELECTOR, "#menu")
    MAIN_FOOTER_B = (By.CSS_SELECTOR, ".col-sm-3")
    MAIN_FOOTER = (By.CSS_SELECTOR, "footer")