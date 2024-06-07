from selenium.webdriver.support.wait import WebDriverWait

from pages.main import AH_main
from pages.search import AH_search
from pages.product import AH_product_page


def test_albert(_browser):
    
    URL = "https://www.ah.nl/"
    SEARCH_NAME = "Pindakaas"
    ITEM_NAME_LINK = []
    ITEM_NUMBER = 2

    wait = WebDriverWait(_browser, 20)
    
    
    main_page = AH_main(_browser)
    main_page.open_page(URL)
    main_page.search(wait, SEARCH_NAME)

    search_page = AH_search(_browser)
    ITEM_NAME_LINK.extend(search_page.open_product(wait, ITEM_NUMBER))
    
    # .click() returns error, thereforth I'm getting link from element and then executing it with script
    _browser.execute_script("window.open('" + ITEM_NAME_LINK[1] +"')")
    
    _browser.switch_to.window(_browser.window_handles[1])

    prod_page = AH_product_page(_browser)

    assert (prod_page.get_product_name() == ITEM_NAME_LINK[0])