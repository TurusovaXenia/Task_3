import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Клик на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_with_offset(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Заполнить поле 'Email'")
    def fill_email_field(self, email):
        self.type_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Заполнить поле 'Пароль'")
    def fill_password_field(self, password):
        self.type_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Клик на кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_with_offset(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Вход в систему")
    def login(self, user_data):
        self.fill_email_field(user_data["email"])
        self.fill_password_field(user_data["password"])
        self.click_login_button()

    @allure.step("Проверка отображения уникального элемента страницы 'Вход'")
    def is_login_button_visible(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_BUTTON)
