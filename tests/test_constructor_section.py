import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("driver")
class TestConstructorTabs:

    def is_tab_active(self, driver, locator):
        el = driver.find_element(*locator)
        return ACTIVE_TAB_CLASS in el.get_attribute("class")

    def test_buns_tab_active_by_default(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert self.is_tab_active(driver, BUNS_TAB)

    def test_switch_to_sauces_tab(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        sauces_tab = driver.find_element(*SAUCES_TAB)
        sauces_tab.click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: self.is_tab_active(driver, SAUCES_TAB))
        assert self.is_tab_active(driver, SAUCES_TAB)

    def test_switch_to_fillings_tab(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        fillings_tab = driver.find_element(*FILLINGS_TAB)
        fillings_tab.click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: self.is_tab_active(driver, FILLINGS_TAB))
        assert self.is_tab_active(driver, FILLINGS_TAB)