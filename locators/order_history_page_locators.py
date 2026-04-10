from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_FORM = (By.CSS_SELECTOR, "ul[class*='OrderHistory_profileList']")
