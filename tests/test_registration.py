import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTRATION_LINK, PASSWORD_INPUT, NAME_INPUT, REGISTER_BUTTON, ERROR_PASSWORD

class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(*REGISTRATION_LINK).click()

    def test_registration_page_loads(self):
        self.wait.until(EC.visibility_of_element_located(PASSWORD_INPUT))

    def test_registration_bad_password(self):
        self.wait.until(EC.visibility_of_element_located(PASSWORD_INPUT))
        self.driver.find_element(*NAME_INPUT).send_keys("Тест Имя")
        self.driver.find_element(*PASSWORD_INPUT).send_keys("123")
        self.driver.find_element(*REGISTER_BUTTON).click()

        error = self.wait.until(EC.visibility_of_element_located(ERROR_PASSWORD))
        assert error.is_displayed(), "Ошибка пароля не показалась при некорректном вводе"
