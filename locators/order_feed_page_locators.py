from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_BOX = (By.CSS_SELECTOR, "div[class*='OrderFeed_contentBox']")
    ORDER_NUMBERS_LIST = (By.CSS_SELECTOR, "div[class*='OrderHistory_textBox'] p[class*='digits']")
    ORDER_NUMBER = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]/p[contains(@class, 'digits')]")
    ORDERS_ON_WORK_LIST = (By.CSS_SELECTOR, "ul[class*='orderListReady'] li[class*='digits']")
    ORDERS_COMPLETED_TOTAL = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDERS_COMPLETED_TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
