from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():
  def __init__(self, browser: webdriver.Chrome, url: str, timeout: int = 10) -> None:
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)

  def open(self) -> None:
    self.browser.get(self.url)

  def is_element_present(self, how: By, what: str) -> bool:
    try:
      self.browser.find_element(how, what)
    except NoSuchElementException:
      return False
    return True