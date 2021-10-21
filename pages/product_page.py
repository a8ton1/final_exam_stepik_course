from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage): 
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def name_product_in_basket(self):
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert name_basket == name, "Name is incorrect"
        
    def price_product_in_basket(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_basket == price, "Price is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"