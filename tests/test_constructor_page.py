import allure

import data


@allure.suite("Страница 'Конструктор'")
class TestConstructorPage:
    @allure.title("Проверка перехода на страницу 'Конструктор' при клике на кнопку 'Конструктор'")
    def test_click_constructor_button_redirects_to_constructor_page(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.header.click_order_feed_button()
        app.header.click_constructor_button()

        assert app.constructor_page.is_burger_construction_section_visible(), \
            "Переход на страницу 'Конструктор заказа' не выполнен"

    @allure.title("Проверка открытия деталей ингредиента при клике на ингредиент")
    def test_click_ingredient_card_opens_ingredient_modal(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.click_first_ingredient_card()

        assert app.constructor_page.is_ingredient_modal_visible(), \
            "Окно с заголовком 'Детали заказа' не открылось"

    @allure.title("Проверка закрытия деталей ингредиента при клике на крестик")
    def test_click_cross_closes_ingredient_modal(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.click_first_ingredient_card()
        app.constructor_page.click_cross_button_for_ingredient_modal()

        assert app.constructor_page.is_ingredient_modal_visible() == False, \
            "Окно с заголовком 'Детали заказа' не закрылось"

    @allure.title("Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ")
    def test_add_ingredient_increases_counter(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.drag_first_ingredient_and_drop_to_basket()

        with allure.step("Проверка увеличения счетчика ингредиента"):
            assert app.constructor_page.get_counter_value_for_first_ingredient() == "2", \
                "Счетчик ингредиента не увеличился при добавлении в заказ"

    @allure.title("Проверка создания заказа для авторизированного пользователя")
    def test_authorized_user_creates_order_successfully(self, app, user):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.click_login_button()
        app.login(user)
        app.constructor_page.drag_first_ingredient_and_drop_to_basket()
        app.constructor_page.click_create_order_button()

        with allure.step("Проверка создания заказа:"):
            assert app.constructor_page.get_order_number() != data.invalid_order_number, \
                "Заказ не был создан"
