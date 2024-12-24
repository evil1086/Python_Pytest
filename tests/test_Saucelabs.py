import pytest
from selenium import webdriver
import time
import pdb

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.sauce_login_page import SauceLabsLogin
from pageObjects.SaucelabsProducts import SauceLabsProducts
from pageObjects.SauceLabsCartpage import SauceLabsCartpage
from pageObjects.SaucelabsUserInfo import SauceLabsUserInfo
from pageObjects.SauceLabscheckout import SauceLabscheckout
from pageObjects.SaucelabsOrderPage import SauceLabsOrderpage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData
# from pageObjects import (SauceLabsLogin, cart_page)
    


class TestSaucelab(BaseClass):
    log = BaseClass.getLogger()

    def test_login(self):
        sauce_lab = SauceLabsLogin(self.driver)
        self.log.info("User landed on the login page")
        login_user = sauce_lab.login_username()
        login_user.clear()
        login_user.send_keys(HomePageData.test_login_details['username'])
        password = sauce_lab.login_pasword()
        password.clear()
        password.send_keys(HomePageData.test_login_details['password'])
        login_button = sauce_lab.login_submit()
        login_button.click()

    def test_products(self):
        sauce_products = SauceLabsProducts(self.driver)
        add_to_cart = sauce_products.add_to_cart()
        add_to_cart.click()
        verify_cart_badge = sauce_products.verify_cart_badge()
        cart_badge_txt = verify_cart_badge.text
        if str(cart_badge_txt) == '1':
            self.log.info('Cart items are accurate on products page')
        else:
            raise AssertionError('Value is not added to the cart')
        
        nav_to_cart = sauce_products.cart_link()
        nav_to_cart.click()

    def test_cart_page(self):
        cart_page = SauceLabsCartpage(self.driver)
        list_of_products = cart_page.verify_cart_items()
        for products in list_of_products:
            prod_details = products.text
            self.log.info("Product details are: {}".format(prod_details))
        verify_cart_count = cart_page.verify_cart_badge()
        cart_badge_txt = verify_cart_count.text
        if str(cart_badge_txt) == '1':
            self.log.info('Cart items are accurate on cart page')
        else:
            raise AssertionError('Value is not added to the cart')
        nav_to_checkout = cart_page.navigate_to_checkout()
        nav_to_checkout.click()

    
    def test_userinfo_page(self):
        user_info_page = SauceLabsUserInfo(self.driver)
        fname = user_info_page.enter_fname()
        fname.send_keys(HomePageData.test_login_details['fname'])
        lname = user_info_page.enter_lname()
        lname.send_keys(HomePageData.test_login_details['lname'])
        zip = user_info_page.enter_zip()
        zip.send_keys(HomePageData.test_login_details['Zip'])
        continue_button_link = user_info_page.nav_to_continue()
        continue_button_link.click()

    def test_checkout_page(self):
        checkout_page = SauceLabscheckout(self.driver)
        verify_cart_badge = checkout_page.verify_cart_badge()
        cart_badge_txt = verify_cart_badge.text
        if str(cart_badge_txt) == '1':
            self.log.info('Cart items are accurate on checkout page')
        else:
            raise AssertionError('Value is not added to the cart')
        summary = checkout_page.verify_summary_details()
        summary_txt = summary.text
        self.log.info("here is the summary: {}".format(summary_txt))
        finish = checkout_page.clickon_finish()
        finish.click()

    def test_order_completion(self):
        order_completion = SauceLabsOrderpage(self.driver)
        completion_txt = order_completion.verify_order_completion()
        success_txt = completion_txt.text
        self.log.info("Received success message as :{}".format(success_txt))
        assert success_txt == "Thank you for your order!"

   