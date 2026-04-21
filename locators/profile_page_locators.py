from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_FORM = (By.CSS_SELECTOR, "div[class*='Profile_profile']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
