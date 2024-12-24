from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceLabsLogin:

    def __init__(self, driver):
        self.driver = driver

    
    # xpaths of the login page
    username = ('user-name')
    password = ('password')
    login_button = ('login-button')

    # navigational/pilot code 
    def login_username(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.username)
    
    def login_pasword(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.password)

    def login_submit(self):
        driver:WebDriver = self.driver
        return driver.find_element(By.ID, self.login_button)



# login = SauceLabsLogin()


