from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class AH_product_page:
    
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):

        name_product = self.driver.find_element(By.CSS_SELECTOR, "div[class^='product-card-header'] span[class^='line-clamp']")

        # Get product name at product page
        # try:
        #     name_product = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class^='product-card-header_root'] span"))
        #     )
        # except exceptions.StaleElementReferenceException as e:
        #     print('{0} >> {1}'.format('name_product', e))

        return name_product.text