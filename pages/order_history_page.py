from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    def is_order_history_form_visible(self):
        self.wait_until_visible(OrderHistoryPageLocators.ORDER_HISTORY_FORM)
        return self.is_element_visible(OrderHistoryPageLocators.ORDER_HISTORY_FORM)

    def get_last_order_number(self):
        orders = self.find_elements_with_wait(OrderHistoryPageLocators.ORDER_NUMBERS_LIST)
        return orders[-1].text
