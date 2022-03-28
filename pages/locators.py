from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')
    BOOK_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    BASKET_PRICE = (By.XPATH, '//*[@class="alert alert-safe alert-noicon alert-info  fade in"]/div/p/strong')
    BOOK_PRICE = (By.XPATH, '//*[@class="col-sm-6 product_main"]/p[@class="price_color"]')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_BLANK_EMAIL = (By.ID, "id_registration-email")
    REGISTER_BLANK_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_BLANK_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')
    BASKET_ITEM = (By.CLASS_NAME, "basket_formset")


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inv")
    VIEW_BASKET_BUTTON = (By.XPATH, '//*[@class="basket-mini pull-right hidden-xs"]/span/a')
