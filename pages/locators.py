from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div:nth-child(1) > .alertinner > strong")
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div:nth-child(3) > .alertinner > p > strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(1) > .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p > a")