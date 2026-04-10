import data


class TestForgotPasswordPage:
    def test_click_forgot_password_link_redirects_to_forgot_password_page(self, app):
        app.home_page.open()
        app.home_page.click_login_button()
        app.login_page.click_forgot_password_link()

        assert app.forgot_password_page.is_reset_password_button_visible(), \
            "Переход на страницу 'Восстановление пароля' не выполнен"

    def test_click_show_password_button_highlights_password_field(self, app):
        app.home_page.open()
        app.home_page.click_login_button()
        app.login_page.click_forgot_password_link()
        app.forgot_password_page.fill_email_field(data.test_email)
        app.forgot_password_page.click_reset_password_button()
        app.forgot_password_page.click_show_password_button()

        assert app.forgot_password_page.is_password_field_highlighted(), \
            "Поле 'Пароль' не подсвечивается при клике на кнопку 'Показать/скрыть пароль'"
