from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.ID, "email-input")
PASSWORD_INPUT = (By.ID, "password-input")
LOGIN_BUTTON = (By.ID, "login-button")
LOGOUT_BUTTON = (By.ID, "logout-button")

BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")
ACTIVE_TAB_CLASS = "tab_tab_type_current__2BEPc"

REGISTRATION_LINK = (By.LINK_TEXT, "Регистрация")
PASSWORD_REG_INPUT = (By.ID, "password")
NAME_INPUT = (By.ID, "name")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
ERROR_PASSWORD = (By.XPATH, "//p[contains(text(), 'пароль')]")