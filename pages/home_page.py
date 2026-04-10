from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def click_login_button(self):
        self.click_element(HomePageLocators.LOGIN_BUTTON)
