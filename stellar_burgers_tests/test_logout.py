import pytest
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_EMAIL = "Vlad_Korolev_29_123@yandex.ru"
TEST_PASSWORD = "dkfl96"

@pytest.fixture
def login(driver):
    def _login():
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.find_element(*EMAIL_LOGIN_INPUT).is_displayed())
        driver.find_element(*EMAIL_LOGIN_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*PASSWORD_LOGIN_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PROFILE_BUTTON))
    return _login

def test_logout(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login()
    driver.find_element(*PROFILE_BUTTON).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/profile"))

    driver.find_element(*LOGOUT_BUTTON).click()
    wait.until(EC.url_contains("/login"))
    assert "Войти" in driver.page_source
