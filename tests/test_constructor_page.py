import data


class TestConstructorPage:
    def test_click_construction_button_redirects_to_constructor_page(self, app):
        app.constructor_page.open()
        app.header.click_order_feed_button()
        app.header.click_constructor_button()

        assert app.constructor_page.is_burger_construction_section_visible(), \
            "Переход на страницу 'Конструктор заказа' не выполнен"

    def test_click_on_ingredient_card_opens_ingredient_modal(self, app):
        app.constructor_page.open()
        app.constructor_page.click_first_ingredient_card()

        assert app.constructor_page.is_ingredient_modal_visible(), \
            "Окно с заголовком 'Детали заказа' не открылось"

    def test_click_on_cross_button_on_ingredient_modal_closes_ingredient_modal(self, app):
        app.constructor_page.open()
        app.constructor_page.click_first_ingredient_card()
        app.constructor_page.click_cross_button_for_ingredient_modal()

        assert app.constructor_page.is_ingredient_modal_visible() == False, \
            "Окно с заголовком 'Детали заказа' не закрылось"

    def test_add_ingredient_to_order_increase_ingredient_counter(self, app):
        app.constructor_page.open()
        app.constructor_page.drag_first_ingredient_and_drop_to_basket()

        assert app.constructor_page.get_counter_value_for_first_ingredient() == "2", \
            "Каунтер ингредиента не увеличился при добавлении в заказ"

    def test_authorized_user_can_create_order(self, app, user_for_test):
        app.constructor_page.open()
        app.login_page.click_login_button()
        app.login(user_for_test)
        app.constructor_page.drag_first_ingredient_and_drop_to_basket()
        app.constructor_page.click_create_order_button()

        assert app.constructor_page.get_order_number()!= data.invalid_order_number, \
            "Заказ не был создан"
