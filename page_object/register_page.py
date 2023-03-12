from selenium.webdriver.common.by import By


class RegisterPage:
    A1 = (By.CSS_SELECTOR, "#input-password")
    A2 = (By.CSS_SELECTOR, "fieldset:nth-child(2)")
    ACCOUNT_LINKS = (By.CSS_SELECTOR, ".list-group")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[type='submit']")
