from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class BasketPageLocators():
    BASKET_EMPTY_TEXT_ELEMENT = (By.CSS_SELECTOR, ".content p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items:nth-of-type(1)")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REGISTER_BUTTON = (
        By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_PRODUCT_NAME = (
        By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    BUSKET_ELEMENT_TEXT = (
        By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
