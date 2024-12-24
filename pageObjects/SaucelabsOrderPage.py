from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceLabsOrderpage:

    def __init__(self, driver):
        self.driver = driver

    
    # xpaths of the Order page
    h2_header = ('complete-header')
   
    # navigational code 

    def verify_order_completion(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.CLASS_NAME, self.h2_header)
    
# orderpage = SauceLabsOrderpage()
    
    