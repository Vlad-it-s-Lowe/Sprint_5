import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTRATION_LINK, PASSWORD_INPUT

class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(*REGISTRATION_LINK).click()

    def test_registration_page_loads(self):
        self.wait.until(EC.visibility_of_element_located(PASSWORD_INPUT))