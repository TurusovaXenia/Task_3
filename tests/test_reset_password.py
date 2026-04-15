import allure

import data


@allure.suite("Страница 'Восстановить пароль'")
class TestResetPasswordPage:
    @allure.title("Проверка подсвечивания поля 'Пароль' при клике на кнопку 'показать/скрыть пароль'")
    def test_click_show_password_button_highlights_password_field(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()
        app.constructor_page.click_login_button()
        app.login_page.click_forgot_password_link()
        app.forgot_password_page.fill_email_field(data.test_email)
        app.forgot_password_page.click_reset_password_button()
        app.reset_password_page.click_show_password_button()

        assert app.reset_password_page.is_password_field_highlighted(), \
            "Поле 'Пароль' не подсвечивается при клике на кнопку 'Показать/скрыть пароль'"
