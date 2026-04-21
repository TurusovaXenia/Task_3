import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Проверка отображения уникального элемента страницы 'Забыли пароль'")
    def is_reset_password_button_visible(self):
        return self.is_element_visible(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step("Заполнить поле 'Email'")
    def fill_email_field(self, email):
        self.type_text(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step("Клик на кнопку 'Восстановить'")
    def click_reset_password_button(self):
        self.click_with_offset(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
