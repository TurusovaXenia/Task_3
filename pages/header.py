import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):
    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_my_profile_button(self):
        self.click_with_offset(HeaderLocators.MY_PROFILE_BUTTON)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_with_offset(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.click_with_offset(HeaderLocators.ORDER_FEED_BUTTON)
