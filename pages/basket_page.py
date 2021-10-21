from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators


class BasketPage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
#        self.browser.implicitly_wait(10)

    def basket_is_not_empty(self, how, what): # Проверка пустая ли корзина, ожидается, что она пустая
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def disappeared_basket_empty(self, how, what, timeout=4): # Антипрроверка путая ли корзина, ожидается, что она не пустая
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_basket_empty(self): # Проверяет пустая ли корзина, если товара нет, то тест зеленый(passed)
        assert self.basket_is_not_empty(*BasketPageLocators.BASKET_EMPTY), \
           "Basket is not empty"

    def should_disappeared_basket_empty(self): # Проверяет пустая ли корзина, если есть товар, то тест зеленый(passed)
        assert self.disappeared_basket_empty(*BasketPageLocators.BASKET_EMPTY), \
           "Basket is empty"