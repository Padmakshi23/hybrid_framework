import pytest
from selenium import webdriver

from Uitilites import read_utilites


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name = read_utilites.get_value_from_json("../test_data/data.json", "browser")

        if browser_name == "edge":
            self.driver = webdriver.Edge()
        elif browser_name == "ch":
            opt = webdriver.ChromeOptions()
            opt.add_argument("start-maximized")
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()