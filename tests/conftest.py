import pytest
from selenium import webdriver
from pages.log_in import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.autodoc.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    log_in = LoginPage(driver)
    log_in.open_private_office_page()
    log_in.do_login('KZM-1539', "23111999")
    return driver

