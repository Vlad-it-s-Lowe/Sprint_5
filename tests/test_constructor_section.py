import pytest
from selenium.webdriver.support.ui import WebDriverWait
from helpers import is_tab_active
from locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB

class TestConstructorTabs:

    def test_buns_tab_active_by_default(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert is_tab_active(driver, BUNS_TAB)

    def test_switch_to_sauces_tab(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        sauces_tab = driver.find_element(*SAUCES_TAB)
        sauces_tab.click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: is_tab_active(driver, SAUCES_TAB))
        assert is_tab_active(driver, SAUCES_TAB)

    def test_switch_to_fillings_tab(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        fillings_tab = driver.find_element(*FILLINGS_TAB)
        fillings_tab.click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: is_tab_active(driver, FILLINGS_TAB))
        assert is_tab_active(driver, FILLINGS_TAB)