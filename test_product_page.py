import pytest
from test_booking.stepik_exam_test.pages.product_page import ProductPage
from test_booking.stepik_exam_test.pages.basket_page import BasketPage
from test_booking.stepik_exam_test.pages.base_page import BasePage
from test_booking.stepik_exam_test.pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
email = str(time.time()) + "@fakemail.org"
password = "123sdfg567hj8"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(email, password, browser)
        base_page = BasePage(browser, link)
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.is_product_name_correct()
        product_page.is_price_correct()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.is_product_name_correct()
    product_page.is_price_correct()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    base_page = BasePage(browser, link)
    base_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    basket_page = BasketPage(browser, link)
    basket_page.go_to_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_disappeared_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

