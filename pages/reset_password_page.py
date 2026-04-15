from selenium.common import TimeoutException

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    def click_show_password_button(self):
        self.click_with_offset(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_highlighted(self):
        try:
            self.wait_for_attribute(ResetPasswordPageLocators.PASSWORD_FIELD_CONTAINER, "class",
                                               "input_status_active")
            return True
        except TimeoutException:
            return False
