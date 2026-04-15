from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    def click_my_profile_button(self):
        self.click_with_offset(HeaderLocators.MY_PROFILE_BUTTON)

    def click_constructor_button(self):
        self.click_with_offset(HeaderLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.click_with_offset(HeaderLocators.ORDER_FEED_BUTTON)
