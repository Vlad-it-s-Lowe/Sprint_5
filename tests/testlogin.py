import pytest
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def test_login_via_main_button(self, driver, login):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        login()
        assert "Личный кабинет" in driver.page_source

    def test_login_via_personal_account_button(self, driver, login):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*PERSONAL_ACCOUNT_BTN).click()
        login()
        assert "Личный кабинет" in driver.page_source

    def test_login_via_register_form(self, driver, login):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_BUTTON_IN_REG))
        driver.find_element(*LOGIN_BUTTON_IN_REG).click()
        login()
        assert "Личный кабинет" in driver.page_source

    def test_login_via_forgot_password_form(self, driver, login):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_BUTTON_IN_FORGOT))
        driver.find_element(*LOGIN_BUTTON_IN_FORGOT).click()
        login()
        assert "Личный кабинет" in driver.page_source