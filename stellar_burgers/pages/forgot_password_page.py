from selenium.common import TimeoutException

from stellar_burgers.locators.forgot_password_page_locators import ForgotPasswordPageLocators
from stellar_burgers.pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def is_reset_password_button_visible(self):
        return self.check_element_visibility(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def fill_email_field(self, email):
        self.fill_input(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    def click_reset_password_button(self):
        self.click_element(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def click_show_password_button(self):
        self.wait_until_invisibility(ForgotPasswordPageLocators.MODAL_OVERLAY)
        self.click_element(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_highlighted(self):
        try:
            self.wait_for_attribute_in_element(ForgotPasswordPageLocators.PASSWORD_FIELD_CONTAINER, "class",
                                               "input_status_active")
            return True
        except TimeoutException:
            return False
