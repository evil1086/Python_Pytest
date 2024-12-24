from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceLabsCartpage:

    def __init__(self, driver):
        self.driver = driver

    
    # xpaths of the Cart page
    cart_item_list = ("//div[@class= 'cart_list']/div[@class= 'cart_item']/descendant::a")
    remove_from_cart_page = ("//div[@class= 'cart_list']/div[@class= 'cart_item']/descendant::a/div[contains(text(), 'Sauce Labs Bike Light')]/ancestor::div[@class= 'cart_item_label']/div[@class= 'item_pricebar']/button")
    cart = ('.shopping_cart_link')
    cart_number = ('shopping_cart_badge')
    checkout = ('checkout')

    # navigational/Pilot code
    def verify_cart_items(self):
        driver:WebDriver = self.driver
        return driver.find_elements(By.XPATH, self.cart_item_list)
    
    def remove_cart_items(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.XPATH, self.remove_from_cart_page)
    
    def verify_cart_badge(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.CLASS_NAME, self.cart_number)
    
    def navigate_to_checkout(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.checkout)
    
# cart_page = SauceLabsCartpage()