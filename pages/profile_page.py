from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def is_profile_form_visible(self):
        self.wait_until_visible(ProfilePageLocators.PROFILE_FORM)
        return self.is_element_visible(ProfilePageLocators.PROFILE_FORM)

    def click_order_history_button(self):
        self.click_with_offset(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_with_offset(ProfilePageLocators.LOGOUT_BUTTON)
