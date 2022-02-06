from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_located(self, locator: tuple):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple):
        self.wait_located(locator).click()
