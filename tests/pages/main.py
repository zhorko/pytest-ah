from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class AH_main:
    
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    # Searches hotel 
    def search(self, wait):
        
        # Click on button 'Search' 
        try:
            wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[class^='search_input']"))
            ).send_keys('pindakaas' + Keys.RETURN)
        except exceptions.ElementNotInteractableException as e:
            print('{0} >> {1}'.format('input_btn', e))