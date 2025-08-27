import pytest
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def login(driver):
    def _login():
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(EMAIL_LOGIN_INPUT))
        driver.find_element(*EMAIL_LOGIN_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*PASSWORD_LOGIN_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PROFILE_BUTTON))
    return _login

def test_navigation_to_personal_account(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login()
    driver.find_element(*PROFILE_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/profile"))
    assert "Профиль" in driver.page_source

def test_navigation_from_profile_to_constructor_and_logo(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login()
    driver.find_element(*PROFILE_BUTTON).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/profile"))

    driver.find_element(*CONSTRUCTOR_BUTTON).click()
    wait.until(EC.url_contains("/"))
    assert "Соберите бургер" in driver.page_source

    driver.find_element(*LOGO_STELLAR).click()
    wait.until(EC.url_contains("/"))
    assert "Соберите бургер" in driver.page_source