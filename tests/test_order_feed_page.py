class TestOrderFeedPage:
    def test_click_order_feed_button_redirects_to_order_feed_page(self, app):
        app.constructor_page.open()
        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_feed_box_visible(), \
            "Переход на страницу 'Лента заказов' не выполнен"