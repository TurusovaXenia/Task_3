from locators.header_locators import HeaderLocators
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class Header(BasePage):
    def click_my_profile_button(self):
        self.click_to_element_with_wait(HeaderLocators.MY_PROFILE_BUTTON)

    def click_constructor_button(self):
        self.click_to_element_with_wait(HeaderLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.click_to_element_with_wait(HeaderLocators.ORDER_FEED_BUTTON)
