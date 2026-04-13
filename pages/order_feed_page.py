from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def is_order_feed_box_visible(self):
        self.wait_until_visible(OrderFeedPageLocators.ORDER_FEED_BOX)
        return self.check_element_visibility(OrderFeedPageLocators.ORDER_FEED_BOX)
