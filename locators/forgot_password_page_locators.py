from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    MODAL_OVERLAY = (By.XPATH, "(.//div[contains(@class, 'Modal_modal_overlay')])[2]")
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button[class*=button]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[class*=input]")
