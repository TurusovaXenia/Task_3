from pages.base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators

class OrderHistoryPage(BasePage):
    def is_order_form_visible(self):
        return self.check_element_visibility(OrderHistoryPageLocators.ORDER_FORM)