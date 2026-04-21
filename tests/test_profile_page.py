import allure


@allure.suite("Страница 'Личный кабинет'")
class TestProfilePage:
    @allure.title("Проверка перехода на страницу 'Профиль' при клике на кнопку 'Личный кабинет'")
    def test_click_profile_button_redirects_to_page(self, app, user):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.click_login_button()
        app.login(user)
        app.header.click_my_profile_button()

        assert app.profile_page.is_profile_form_visible(), \
            "Переход на страницу 'Профиль' не выполнен"

    @allure.title("Проверка перехода на страницу 'История заказов' при клике на кнопку 'История заказов'")
    def test_click_order_history_button_redirects_to_page(self, app, created_order):
        app.header.click_my_profile_button()
        app.profile_page.click_order_history_button()

        assert app.orders_history_page.is_order_history_form_visible(), \
            "Переход на страницу 'История заказов' не выполнен"

    @allure.title("Проверка выхода из системы при клике на кнопку 'Выход'")
    def test_click_logout_button_redirects_to_login(self, app, user):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.click_login_button()
        app.login(user)
        app.header.click_my_profile_button()
        app.profile_page.click_logout_button()

        assert app.login_page.is_login_button_visible(), \
            "Переход на страницу 'Вход' не выполнен"
