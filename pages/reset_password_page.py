from selenium.common import TimeoutException

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
import allure

class ResetPasswordPage(BasePage):
    @allure.step("Клик по кнопке 'показать/скрыть пароль'")
    def click_show_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка подсвечивания поля 'Пароль'")
    def is_password_field_highlighted(self):
        try:
            self.wait_for_attribute(ResetPasswordPageLocators.PASSWORD_FIELD_CONTAINER, "class",
                                               "input_status_active")
            return True
        except TimeoutException:
            return False
