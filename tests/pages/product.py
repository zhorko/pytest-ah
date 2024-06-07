from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class AH_main:
    
    def __init__(self, driver):
        self.driver = driver

    def get_product_name (self, wait):

        # Get product name at product page
        try:
            name_product = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class^='product-card-header_root'] span"))
            )
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format('item_search', e))