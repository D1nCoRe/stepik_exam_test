from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_IN_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_element_disappeared(*ProductPageLocators.BOOK_NAME_IN_SUCCESS_MESSAGE), \
            "Success message didn't disappear"

    def is_product_name_correct(self):
        name_in_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((
            ProductPageLocators.BOOK_NAME_IN_SUCCESS_MESSAGE))).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert name_in_message == book_name, "Real name and message name don't match"

    def is_price_correct(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_price, "Book price and basket price don't match"
