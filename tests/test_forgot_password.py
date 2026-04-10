class TestForgotPasswordPage:
    def test_click_forgot_password_link_redirects_to_forgot_password_page(self, app):
        app.home_page.open()
        app.home_page.click_login_button()
        app.login_page.click_forgot_password_link()

        assert app.forgot_password_page.is_reset_password_button_visible(), \
            "Переход на страницу 'Восстановление пароля' не выполнен"
