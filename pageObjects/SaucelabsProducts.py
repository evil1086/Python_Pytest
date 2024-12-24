from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceLabsProducts:

    def __init__(self, driver):
        self.driver = driver

    
    # xpaths of the login page
    addtocart = ("//div[@class= 'inventory_item_name ' and contains(text(), 'Sauce Labs Onesie')]/ancestor::div[@class= 'inventory_item_description']/descendant::div[@class= 'pricebar']/button[contains(text(), 'Add to cart')]")
    remove = ("//div[@class= 'inventory_item_name ' and contains(text(), 'Sauce Labs Onesie')]/ancestor::div[@class= 'inventory_item_description']/descendant::div[@class= 'pricebar']/button[contains(text(), 'Remove')] ")
    cart = ('.shopping_cart_link')
    cart_number = ('.shopping_cart_badge')

    # navigational code
    def add_to_cart(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.XPATH, self.addtocart)
    
    def remove_from_cart(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.XPATH, self.remove)
    
    def cart_link(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.CSS_SELECTOR, self.cart)
    
    def verify_cart_badge(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.CSS_SELECTOR, self.cart_number)
    

# products_page = SauceLabsProducts()