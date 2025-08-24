import pytest
from locators import *
from selenium.webdriver.common.by import By
import time

def test_constructor_tabs_work(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    buns_tab = driver.find_element(*BUNS_TAB)
    buns_tab.click()
    time.sleep(1)  # небольшой простой для переключения вкладки
    assert "Булки" in buns_tab.text

    sauces_tab = driver.find_element(*SAUCES_TAB)
    sauces_tab.click()
    time.sleep(1)
    assert "Соусы" in sauces_tab.text

    fillings_tab = driver.find_element(*FILLINGS_TAB)
    fillings_tab.click()
    time.sleep(1)
    assert "Начинки" in fillings_tab.text
