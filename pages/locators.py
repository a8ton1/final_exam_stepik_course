from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "#register_form_inc")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_inc")