from selenium.webdriver.common.by import By

from Base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        self.__username_locator = (By.NAME, "username")
        self.__password_locator = (By.NAME, "password")
        self.__login_locator = (By.XPATH, "//button[normalize-space()='Login']")

    def enter_username(self, username):
        # self.driver.find_element(By.NAME, "username").send_keys(username)
        self.type_by_locator(self.__username_locator, username)

    def enter_password(self, password):
        # self.driver.find_element(By.NAME, "password").send_keys(password)
        self.type_by_locator(self.__password_locator, password)

    def click_on_login(self):
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.click_by_locator(self.__login_locator)

    @property
    def get_invalid_error_message(self):
        return self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text

    @property
    def get_username_placeholder(self):
        return self.get_attribute_value(self.__username_locator, "placeholder")

    @property
    def get_password_placeholder(self):
        return self.get_attribute_value(self.__password_locator, "placeholder")
