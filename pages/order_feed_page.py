from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def is_order_feed_box_visible(self):
        self.wait_until_visible(OrderFeedPageLocators.ORDER_BOX)
        return self.check_element_visibility(OrderFeedPageLocators.ORDER_BOX)

    def click_order_card_with_order_number(self, order_number):
        order = self.get_element_from_list_by_containing_text(OrderFeedPageLocators.ORDER_NUMBERS_LIST, order_number)
        self.click_to_element(order)

    def get_order_number_from_card(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_NUMBER)

    def is_order_in_feed(self, order_number):
        return self.wait_for_text_in_list(OrderFeedPageLocators.ORDER_NUMBERS_LIST, order_number)

    def is_order_in_orders_on_work_list(self, order_number):
        return self.wait_for_text_in_list(OrderFeedPageLocators.ORDERS_ON_WORK_LIST, order_number)
