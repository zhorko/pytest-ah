import pytest
from selenium import webdriver

@pytest.fixture()
def _browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()