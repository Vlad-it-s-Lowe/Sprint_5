import pytest
from locators import *
from utils import generate_email, generate_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("name,email,password", [
    ("Тест Имя", generate_email(), generate_password(6))
])

def test_successful_registration(driver, name, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Регистрация").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(NAME_INPUT))
    driver.find_element(*NAME_INPUT).send_keys(name)
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)

    driver.find_element(*REGISTER_BUTTON).click()

    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url

def test_registration_bad_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Регистрация").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibilityofelementlocated(PASSWORDINPUT))
    driver.findelement(*NAMEINPUT).sendkeys("Тест Имя")
    driver.findelement(EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(PASSWORDINPUT).sendkeys("123")

    driver.findelement(*REGISTERBUTTON).click()

    error = wait.until(EC.visibilityofelementlocated(ERRORPASSWORD))
    assert error.isdisplayed()
