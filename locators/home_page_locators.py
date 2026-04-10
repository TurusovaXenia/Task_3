from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class*=button]")
    MODAL_OVERLAY = (By.XPATH, "(.//div[contains(@class, 'Modal_modal_overlay')])[2]")
