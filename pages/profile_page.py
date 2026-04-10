from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def is_profile_form_visible(self):
        return self.check_element_visibility(ProfilePageLocators.PROFILE_FORM)

    def click_order_history_button(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
