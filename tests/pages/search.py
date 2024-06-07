from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class AH_search:

    def __init__(self, driver):
        self.driver = driver

    # Searches product 
    def open_product(self, wait, index_product_from_list):
        
        if index_product_from_list == 1:
            pass
        elif index_product_from_list == 2:
            index_product_from_list += 1
        elif index_product_from_list == 4:
            index_product_from_list += 1

        # Get nth element from list of products
        try:
            web_elem = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-lane-wrapper article:nth-of-type(" + str(index_product_from_list) + ") a"))
            )
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format('web_elem', e))

        # Get name of selected product
        try:
            name_search = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-lane-wrapper article:nth-of-type(" + str(index_product_from_list) + ") div[class^='body_root'] span"))
            )
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format('name_search', e))

        product_link = web_elem.get_attribute("href")

        return [name_search.text, product_link]