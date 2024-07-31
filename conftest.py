from selenium import webdriver
import pytest
from constants import Constants

@pytest.fixture()
def driver():
   driver = webdriver.Firefox()
   driver.get(Constants.MAIN_URL)
   yield driver
   driver.quit()

