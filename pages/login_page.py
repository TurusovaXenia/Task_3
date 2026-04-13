from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def fill_email_field(self, email):
        self.fill_input(LoginPageLocators.EMAIL_FIELD, email)

    def fill_password_field(self, password):
        self.fill_input(LoginPageLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, user_data):
        self.fill_email_field(user_data["email"])
        self.fill_password_field(user_data["password"])
        self.click_login_button()

    def is_login_button_visible(self):
        return self.check_element_visibility(LoginPageLocators.LOGIN_BUTTON)
