from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_HISTORY_FORM = (By.CSS_SELECTOR, "ul[class*='OrderHistory_profileList']")
    ORDER_NUMBERS_LIST = (By.CSS_SELECTOR, "div[class*=OrderHistory_textBox] p[class*='digits']")
