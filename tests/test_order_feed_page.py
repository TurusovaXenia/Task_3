class TestOrderFeedPage:
    def test_click_order_feed_button_redirects_to_order_feed_page(self, app):
        app.constructor_page.open()
        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_feed_box_visible(), \
            "Переход на страницу 'Лента заказов' не выполнен"

    def test_click_order_card_opens_order_details(self, app, created_order):
        app.header.click_order_feed_button()
        app.order_feed_page.click_order_card_with_order_number(created_order)

        assert created_order in app.order_feed_page.get_order_number_from_card()

    def test_order_from_order_history_page_displays_on_order_feed_page(self, app, created_order):
        app.header.click_my_profile_button()
        app.profile_page.click_order_history_button()
        last_order_number = app.orders_history_page.get_last_order_number()
        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_in_feed(last_order_number), \
            "Последний заказ со страницы 'История заказов' не показывается на странице 'Лента заказов'"

    def test_created_order_displays_on_order_on_work_list(self, app, created_order):
        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_in_orders_on_work_list(created_order), \
            "Созданный заказ не находится в списке 'В работе'"