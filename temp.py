from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

from time import sleep 


def test_temp (_browser):
    
    _browser.get("https://www.ah.nl/")
    wait = WebDriverWait(_browser, 20)
    _browser.maximize_window()


    try:
        input_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[class^='search_input']"))
        ).send_keys('pindakaas' + Keys.RETURN)
    except exceptions.ElementNotInteractableException as e:
        print('{0} >> {1}'.format('input_btn', e))

    first_product = WebDriverWait(_browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#search-lane article:nth-child(1) a')))

    first_product.click()

    # try:
    #     item_search = wait.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-lane-wrapper article:nth-of-type(1) a"))
    #     )
    # except exceptions.StaleElementReferenceException as e:
    #     print('{0} >> {1}'.format('item_search', e))

    try:
        name_search = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-lane-wrapper article:nth-of-type(1) div[class^='body_root'] span"))
        )
    except exceptions.StaleElementReferenceException as e:
        print('{0} >> {1}'.format('item_search', e))

    item_name = name_search.text 
    print(f"{name_search.text = }")

    _browser.execute_script("window.open('" + first_product.get_attribute("href") +"')")

    _browser.switch_to.window(_browser.window_handles[1])

    try:
        name_product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class^='product-card-header_root'] span"))
        )
    except exceptions.StaleElementReferenceException as e:
        print('{0} >> {1}'.format('item_search', e))

    print(f"{name_product.text = }")

    assert name_product.text == item_name
