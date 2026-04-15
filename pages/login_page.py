from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def click_forgot_password_link(self):
        self.click_with_offset(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def fill_email_field(self, email):
        self.type_text(LoginPageLocators.EMAIL_FIELD, email)

    def fill_password_field(self, password):
        self.type_text(LoginPageLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_with_offset(LoginPageLocators.LOGIN_BUTTON)

    def login(self, user_data):
        self.fill_email_field(user_data["email"])
        self.fill_password_field(user_data["password"])
        self.click_login_button()

    def is_login_button_visible(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_BUTTON)
