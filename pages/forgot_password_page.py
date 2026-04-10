from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def is_reset_password_button_visible(self):
        return self.check_element_visibility(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def fill_email_field(self, email):
        self.fill_input(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    def click_reset_password_button(self):
        self.click_element(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
