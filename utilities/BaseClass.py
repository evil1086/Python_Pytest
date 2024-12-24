import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def waitUntilVisible(driver, webElementType, webElement, timeout=20):
        element = 0
        try:
            wait = WebDriverWait(driver, timeout)
            if webElementType == "CSS":
                element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, webElement)))
            elif webElementType == "LINK_TEXT":
                element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, webElement)))
            elif webElementType == "ID":
                element = wait.until(EC.visibility_of_element_located((By.ID, webElement)))
            else:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, webElement)))
        except (NoSuchElementException, ElementNotInteractableException) as error:
            logging.error(f"Web element {webElement} not found NoSuchElementException or  ElementNotInteractableException")
            assert False, f"FAILED: webelement {webElement}failed to load"
        except TimeoutException as err:
            logging.error(f"Web element {webElement} not found Timeout")
            assert False, f"FAILED: {webElement}due to timeout "
        except InvalidArgumentException as e:
            logging.error("Web element not found InvalidArgumentException")
            assert False, "FAILED: InvalidArgumentException "
        return element
    
    def waitUntilClickable(driver, webElementName, webElement, timeout=20):
        element = 0
        try:
            wait = WebDriverWait(driver, timeout)
            if webElementName == "CSS":
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, webElement)))
            elif webElementName == "LINK_TEXT":
                element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, webElement)))
            elif webElementName == "ID":
                element = wait.until(EC.element_to_be_clickable((By.ID, webElement)))
            elif webElementName == "ClassName":
                element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, webElement)))
            else:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, webElement)))
        except (NoSuchElementException, ElementNotInteractableException) as error:
            logging.error("Web element not found NoSuchElementException or  ElementNotInteractableException")
            assert False, "FAILED: webelement failed to load "
        except TimeoutException as err:
            logging.error("Web element not found Timeout")
            #assert False, "FAILED: due to timeout "
        except InvalidArgumentException as e:
            logging.error("Web element not found InvalidArgumentException")
            assert False, "FAILED: InvalidArgumentException "
        return element