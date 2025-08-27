from locators import *

def is_tab_active(driver, locator):
    el = driver.find_element(*locator)
    return ACTIVE_TAB_CLASS in el.get_attribute("class")