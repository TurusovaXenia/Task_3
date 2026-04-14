from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button[class*=button]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[class*=input]")
