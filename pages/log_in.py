from pages.Base import BasePageObject
from selenium.webdriver.common.by import By


class LoginPage(BasePageObject):
    private_office_link = (By.XPATH, "//a[text()='Личный кабинет']")
    login_input = (By.ID, 'Login')
    password_input = (By.ID, 'Password')
    enter_button = (By.CLASS_NAME, "button-red")

    def open_private_office_page(self):
        self.click(self.private_office_link)

    def do_login(self, login, password):
        self.wait_located(self.login_input).send_keys(login)
        self.wait_located(self.password_input).send_keys(password)
        self.click(self.enter_button)


class SelectingTheOriginalDirectory(BasePageObject):
    tree_strips = (By.ID, 'overlay-menu')
    original_catalog = (By.XPATH, "//a[text()='Оригинальный каталог']")

    def overlay_menu(self):
        self.click(self.tree_strips)

    def open_original_catalog(self):
        self.click(self.original_catalog)


class SearchAuto(BasePageObject):
    vin_input = (By.XPATH, "//input[@placeholder='VIN (или FRAME)']")
    search_button = (By.XPATH, "//a[@class='button-vin']")

    def search_by_vin(self, vin):
        self.wait_located(self.vin_input).send_keys(vin)
        self.click(self.search_button)


class OutputComparison(BasePageObject):
    header_text = (By.XPATH, "//p[@class='notice-text']")

    def get_header_text(self):
        return self.wait_located(self.header_text).text
