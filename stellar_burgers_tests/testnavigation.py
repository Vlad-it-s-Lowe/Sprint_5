import pytest
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expectedconditions as EC

TESTEMAIL = "Vlad_Korolev_29_123@yandex.ru"
TESTPASSWORD = "dkfl96"

@pytest.fixture
def login(driver):
    def login():
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibilityofelementlocated(EMAILLOGININPUT))
        driver.findelement(*EMAILLOGININPUT).sendkeys(TESTEMAIL)
        driver.findelement(PASSWORD_LOGIN_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(LOGINSUBMITBUTTON).click()
        wait.until(EC.visibilityofelementlocated(PROFILEBUTTON))
    return login

def testnavigationtopersonalaccount(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login()
    driver.findelement(PROFILE_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/profile"))
    assert "Профиль" in driver.page_source

def test_navigation_from_profile_to_constructor_and_logo(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login()
    driver.find_element(PROFILEBUTTON).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.urlcontains("/profile"))

    driver.findelement(*CONSTRUCTORBUTTON).click()
    wait.until(EC.urlcontains("/"))
    assert "Соберите бургер" in driver.pagesource

    driver.findelement(*LOGOSTELLAR).click()
    wait.until(EC.urlcontains("/"))
    assert "Соберите бургер" in driver.pagesource