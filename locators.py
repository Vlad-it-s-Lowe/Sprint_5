from selenium.webdriver.common.by import By

# --- Регистрация ---
NAME_INPUT = (By.NAME, "name")                           # Поле "Имя"
EMAIL_INPUT = (By.NAME, "email")                         # Поле "Email"
PASSWORD_INPUT = (By.NAME, "password")                   # Поле "Пароль"
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
ERROR_PASSWORD = (By.XPATH, "//*[contains(text(),'пароль')]")  # Сообщение об ошибке пароля

# --- Вход ---
LOGIN_BUTTON_MAIN = (By.LINK_TEXT, "Войти в аккаунт")    # Кнопка "Войти в аккаунт" на главной
PERSONAL_ACCOUNT_BTN = (By.LINK_TEXT, "Личный кабинет")  # Кнопка "Личный кабинет"
LOGIN_BUTTON_IN_REG = (By.LINK_TEXT, "Войти")            # Кнопка "Войти" в форме регистрации
LOGIN_BUTTON_IN_FORGOT = (By.LINK_TEXT, "Войти")         # Кнопка "Войти" в форме восстановления пароля
EMAIL_LOGIN_INPUT = (By.NAME, "email")                   # Email для входа
PASSWORD_LOGIN_INPUT = (By.NAME, "password")             # Пароль для входа
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" для входа

# --- Переходы ---
PROFILE_BUTTON = (By.LINK_TEXT, "Личный кабинет")        # "Личный кабинет"
CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")       # Кнопка "Конструктор"
LOGO_STELLAR = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")  # Логотип

# --- Выход ---
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")   # Кнопка "Выйти" в личном кабинете

# --- Конструктор ---
BUNS_TAB = (By.XPATH, "//span[text()='Булки']")          # Вкладка "Булки"
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")        # Вкладка "Соусы"
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")    # Вкладка "Начинки"