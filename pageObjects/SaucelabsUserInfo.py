from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceLabsUserInfo:

    def __init__(self, driver):
        self.driver = driver

    
    # xpaths of the login page
    fname = ('first-name')
    lname = ('last-name')
    zip = ('postal-code')
    continue_button = ('continue')

    # navigational code
    def enter_fname(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.fname)
    
    def enter_lname(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.lname)
    
    def enter_zip(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.zip)
    
    def nav_to_continue(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.continue_button)
    
# user_info = SauceLabsUserInfo()