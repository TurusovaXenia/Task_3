from stellar_burgers.locators.login_page_locators import LoginPageLocators
from stellar_burgers.pages.base_page import BasePage


class LoginPage(BasePage):
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
