from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT_ELEMENT), "Basket not empty"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM), "There are products in the basket"
