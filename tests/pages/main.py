from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class Trivago_Main:
    
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    # Searches hotel 
    def search(self, wait):
        
        # Click on button 'Search' 
        try:
            wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ""))
            ).click()
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('search_main', e))