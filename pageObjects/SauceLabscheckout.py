from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceLabscheckout:

    def __init__(self, driver):
        self.driver = driver

    
    # xpaths of the Checkout page
    finish = ('finish')
    cart_number = ('shopping_cart_badge')
    summary_page = ('summary_info')
    continue_button = ('continue')

    # navigational/ Pilot code
    def clickon_finish(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.finish)
    
    def verify_cart_badge(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.CLASS_NAME, self.cart_number)
    
    def verify_summary_details(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.CLASS_NAME, self.summary_page)
    
# checkout = SauceLabscheckout()