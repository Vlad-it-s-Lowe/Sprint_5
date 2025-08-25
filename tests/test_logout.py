import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("driver")
class TestLogout:

    def test_logout(self, driver, test_user):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*EMAIL_INPUT).send_keys(test_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(test_user["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON))

        driver.find_element(*LOGOUT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
        assert driver.find_element(*LOGIN_BUTTON).is_displayed()