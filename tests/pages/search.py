from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class AH_search:

    def __init__(self, driver):
        self.driver = driver

    # Searches hotel 
    def get_product(self, wait, product_from_list):
        
        # Get nth element from list of products
        try:
            item_search = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-lane-wrapper article:nth-of-type(" + product_from_list + ") a"))
            )
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format('item_search', e))

        # Get name of selected product
        try:
            name_search = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-lane-wrapper article:nth-of-type(" + product_from_list + ") div[class^='body_root'] span"))
            )
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format('item_search', e))

        product_name = name_search.text 

        return [product_name, item_search]