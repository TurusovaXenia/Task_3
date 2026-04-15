import allure

import data
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step("Клик на кнопку 'Войти'")
    def click_login_button(self):
        self.click_with_offset(ConstructorPageLocators.LOGIN_BUTTON)

    def wait_for_load(self):
        self.wait_until_visible(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Проверка отображения уникального элемента страницы 'Конструктор'")
    def is_burger_construction_section_visible(self):
        return self.is_element_visible(ConstructorPageLocators.BURGER_CONSTRUCTION_SECTION)

    @allure.step("Клик на первый ингредиент на странице 'Конструктор'")
    def click_first_ingredient_card(self):
        self.click_with_offset(ConstructorPageLocators.FIRST_INGREDIENT_CARD)

    @allure.step("Проверка отображения окна с деталями ингредиента")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP_HEADER)

    @allure.step("Клик на крестик")
    def click_cross_button_for_ingredient_modal(self):
        self.click_element(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP_CROSS_BUTTON)
        self.wait_until_invisible(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP_HEADER)

    @allure.step("Выбрать первый ингредиент и добавить его в заказ")
    def drag_first_ingredient_and_drop_to_basket(self):
        ingredient = self.find_element_with_wait(ConstructorPageLocators.FIRST_INGREDIENT_CARD)
        basket = self.find_element_with_wait(ConstructorPageLocators.BURGER_CONSTRUCTION_SECTION)
        self.drag_and_drop(ingredient, basket)

    @allure.step("Получить значение каунтера для первого ингредиента")
    def get_counter_value_for_first_ingredient(self):
        return self.get_text(ConstructorPageLocators.FIRST_INGREDIENT_COUNTER)

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_create_order_button(self):
        self.click_with_offset(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.wait_for_valid_text(ConstructorPageLocators.ORDER_NUMBER, data.invalid_order_number)
        return self.get_text(ConstructorPageLocators.ORDER_NUMBER)

    @allure.step("Клик на крестик")
    def click_cross_button_for_order(self):
        self.wait_for_valid_text(ConstructorPageLocators.ORDER_NUMBER, data.invalid_order_number)
        self.click_with_offset(ConstructorPageLocators.ORDER_POPUP_CROSS_BUTTON)
