import allure


@allure.suite("Страница 'Забыли пароль'")
class TestForgotPasswordPage:
    @allure.title("Проверка перехода на страницу 'Забыли пароль' при клике на ссылку 'Восстановить пароль'")
    def test_click_forgot_password_link_redirects_to_page(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()
        app.constructor_page.click_login_button()
        app.login_page.click_forgot_password_link()

        assert app.forgot_password_page.is_reset_password_button_visible(), \
            "Переход на страницу 'Восстановление пароля' не выполнен"
