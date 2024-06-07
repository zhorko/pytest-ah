from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_WORD = "Pindakaas"

def test_search(_browser):
    _browser.get('https://ah.nl')
    wait = WebDriverWait(_browser, 10)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[class^="search_input"]'))).send_keys(SEARCH_WORD, Keys.ENTER)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#search-lane article:nth-child(1)'))).click()

    assert EC.title_contains(SEARCH_WORD)
