from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class*='button']")
