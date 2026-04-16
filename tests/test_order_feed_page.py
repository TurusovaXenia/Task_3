import allure
import pytest

from locators.order_feed_page_locators import OrderFeedPageLocators


@allure.suite("Страница 'Лента заказов'")
class TestOrderFeedPage:
    @allure.title("Проверка перехода на страницу 'Лента заказов' при клике на кнопку 'Лента заказов'")
    def test_click_order_feed_button_redirects_to_page(self, app):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_feed_box_visible(), \
            "Переход на страницу 'Лента заказов' не выполнен"

    @allure.title("Проверка открытия заказа при клике на карточку заказа на странице 'Лента заказов'")
    def test_click_order_card_opens_modal(self, app, created_order):
        app.header.click_order_feed_button()
        app.order_feed_page.click_order_card_with_order_number(created_order)

        with allure.step("Проверка открытия карточки для созданного заказа:"):
            assert created_order in app.order_feed_page.get_order_number_from_card()

    @allure.title("Проверка отображения заказа из страницы 'История заказов' на странице 'Лента заказов'")
    def test_order_history_item_appears_in_feed(self, app, created_order):
        app.header.click_my_profile_button()
        app.profile_page.click_order_history_button()
        last_order_number = app.orders_history_page.get_last_order_number()
        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_in_feed(last_order_number), \
            "Последний заказ со страницы 'История заказов' не показывается на странице 'Лента заказов'"

    @allure.title("Проверка добавления только что созданного заказа в список 'В работе' на странице 'Лента заказов'")
    def test_created_order_appears_in_work_list(self, app, created_order):
        app.header.click_order_feed_button()

        assert app.order_feed_page.is_order_in_orders_on_work_list(created_order), \
            "Созданный заказ не находится в списке 'В работе'"

    @pytest.mark.parametrize("counter",
        [
            OrderFeedPageLocators.ORDERS_COMPLETED_TOTAL,
            OrderFeedPageLocators.ORDERS_COMPLETED_TODAY
        ],
        ids=["increases_total_counter", "increases_today_counter"]
    )
    @allure.title("Проверка увеличения счетчиков на странице 'Лента заказов' при создании заказа")
    def test_create_order(self, app, user, counter):
        with allure.step("Открыть страницу 'Конструктор'"):
            app.constructor_page.open()

        app.constructor_page.click_login_button()
        app.login(user)

        app.header.click_order_feed_button()
        before_order_creation_counter_value = app.order_feed_page.get_counter_value(counter)

        app.header.click_constructor_button()
        app.constructor_page.drag_first_ingredient_and_drop_to_basket()
        app.constructor_page.click_create_order_button()
        app.constructor_page.click_cross_button_for_order()

        app.header.click_order_feed_button()
        after_order_creation_counter_value = app.order_feed_page.get_counter_value(counter)

        with allure.step("Проверка увеличения значения счетчика"):
            assert after_order_creation_counter_value > before_order_creation_counter_value
