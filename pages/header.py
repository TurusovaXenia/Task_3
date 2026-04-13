from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class Header(BasePage):
    def click_my_profile_button(self):
        self.wait_until_invisibility(HomePageLocators.MODAL_OVERLAY)
        self.click_element(HeaderLocators.MY_PROFILE_BUTTON)

    def click_constructor_button(self):
        self.wait_until_invisibility(HomePageLocators.MODAL_OVERLAY)
        self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.wait_until_invisibility(HomePageLocators.MODAL_OVERLAY)
        self.click_element(HeaderLocators.ORDER_FEED_BUTTON)
