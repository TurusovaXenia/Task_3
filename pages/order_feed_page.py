import allure

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Проверка отображения уникального элемента страницы 'Лента заказов'")
    def is_order_feed_box_visible(self):
        self.wait_until_visible(OrderFeedPageLocators.ORDER_BOX)
        return self.is_element_visible(OrderFeedPageLocators.ORDER_BOX)

    @allure.step("Клик на карточку созданного заказа")
    def click_order_card_with_order_number(self, order_number):
        order = self.get_element_from_list_by_text(OrderFeedPageLocators.ORDER_NUMBERS_LIST, order_number)
        self.click_existing_element(order)

    @allure.step("Получить номер заказа из карточки заказа")
    def get_order_number_from_card(self):
        return self.get_text(OrderFeedPageLocators.ORDER_NUMBER)

    @allure.step("Проверка отображения заказа из страницы 'История заказов' на странице 'Лента заказов'")
    def is_order_in_feed(self, order_number):
        return self.wait_for_text_in_list(OrderFeedPageLocators.ORDER_NUMBERS_LIST, order_number)

    @allure.step("Проверка отображения созданного заказа в списке 'В работе' на странице 'Лента заказов'")
    def is_order_in_orders_on_work_list(self, order_number):
        return self.wait_for_text_in_list(OrderFeedPageLocators.ORDERS_ON_WORK_LIST, order_number)

    @allure.step("Получение значения каунтера из страницы 'Лента заказов'")
    def get_counter_value(self, locator):
        return self.get_text(locator)
