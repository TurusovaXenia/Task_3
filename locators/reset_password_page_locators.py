from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_FIELD_CONTAINER = (By.XPATH, "(.//div[@class='input__container'])[1]/div")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div[class*='input__icon'] svg")
