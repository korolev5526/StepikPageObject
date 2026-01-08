import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
  parser.addoption("--language", action="store", default="en", help="Choose language: ")

@pytest.fixture(scope="function")
def browser(request):
  print("\nЗапуск браузера")
  lang = request.config.getoption("language")
  options = Options()
  options.add_experimental_option('prefs', {'intl.accept_languages': lang})
  browser = webdriver.Chrome(options=options)
  yield browser

  print('\nЗавершение работы браузера')
  browser.quit()

  