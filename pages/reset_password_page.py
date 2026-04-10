from selenium.common import TimeoutException

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    def click_show_password_button(self):
        self.wait_until_invisibility(ForgotPasswordPageLocators.MODAL_OVERLAY)
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_highlighted(self):
        try:
            self.wait_for_attribute_in_element(ResetPasswordPageLocators.PASSWORD_FIELD_CONTAINER, "class",
                                               "input_status_active")
            return True
        except TimeoutException:
            return False
