import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expectedconditions as EC
from locators import EMAILINPUT, PASSWORDINPUT, LOGINBUTTON, LOGOUTBUTTON

@pytest.mark.usefixtures("driver", "testuser")
class TestLogout:

    def testlogout(self, driver, testuser):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.findelement(EMAIL_INPUT).send_keys(test_user["email"])
        driver.find_element(PASSWORDINPUT).sendkeys(testuser["password"])
        driver.findelement(LOGIN_BUTTON).click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON))

        driver.find_element(LOGOUTBUTTON).click()

        wait.until(EC.visibilityofelementlocated(LOGINBUTTON))
        assert driver.findelement(LOGIN_BUTTON).is_displayed()