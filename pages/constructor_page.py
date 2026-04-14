from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def click_login_button(self):
        self.click_element(ConstructorPageLocators.LOGIN_BUTTON)

    def wait_for_load(self):
        self.wait_until_visible(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    def is_burger_construction_section_visible(self):
        return self.check_element_visibility(ConstructorPageLocators.BURGER_CONSTRUCTION_SECTION)

    def click_first_ingredient_card(self):
        self.click_element(ConstructorPageLocators.FIRST_INGREDIENT_CARD)

    def is_ingredient_modal_visible(self):
        return self.check_element_visibility(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP_HEADER)

    def click_cross_button_for_ingredient_modal(self):
        self.click_element(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP_CROSS_BUTTON)
        self.wait_until_invisibility(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP_HEADER)

    def drag_first_ingredient_and_drop_to_basket(self):
        ingredient = self.find_element_with_wait(ConstructorPageLocators.FIRST_INGREDIENT_CARD)
        basket = self.find_element_with_wait(ConstructorPageLocators.BURGER_CONSTRUCTION_SECTION)
        self.drag_and_drop(ingredient, basket)

    def get_counter_value_for_first_ingredient(self):
        return self.get_text_from_element(ConstructorPageLocators.FIRST_INGREDIENT_COUNTER)

    def click_create_order_button(self):
        self.click_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    def get_order_id(self):
        self.wait_until_invisibility(ConstructorPageLocators.LOADER_ON_CREATE_ORDER_POPUP)
        self.wait_for_valid_text(ConstructorPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(ConstructorPageLocators.ORDER_ID)

    def click_cross_button_for_order(self):
        self.click_to_element_with_wait(ConstructorPageLocators.ORDER_POPUP_CROSS_BUTTON)
