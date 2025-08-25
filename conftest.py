import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_EMAIL = "Vlad_Korolev_29_123@yandex.ru"
TEST_PASSWORD = "dkfl96"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def test_user():
    return {"email": TEST_EMAIL, "password": TEST_PASSWORD}

@pytest.fixture
def login(driver, test_user):
    def _login():
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "email-input")))
        driver.find_element(By.ID, "email-input").send_keys(test_user["email"])
        driver.find_element(By.ID, "password-input").send_keys(test_user["password"])
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.visibility_of_element_located((By.ID, "logout-button")))
    return _login