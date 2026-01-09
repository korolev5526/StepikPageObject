from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
  def add_product_to_busket(self):
    add_to_busket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
    add_to_busket_btn.click()
    
  def check_added_to_busket_product_name(self):
    product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
    assert product_name == added_product_name, "The item added to the busket is not the correct one"

  def check_added_to_busket_product_price(self):
    product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    product_price_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT).text
    busket_elem_text = self.browser.find_element(*ProductPageLocators.BUSKET_ELEMENT_TEXT).text
    assert product_price == product_price_in_alert and (product_price in busket_elem_text), "The price of the added product is different"
