from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def click_login_button(self):
        self.click_element(HomePageLocators.LOGIN_BUTTON)

    def wait_for_load(self):
        self.wait_until_visible(HomePageLocators.CREATE_ORDER_BUTTON)

    def is_burger_construction_section_visible(self):
        return self.check_element_visibility(HomePageLocators.BURGER_CONSTRUCTION_SECTION)

    def click_first_ingredient_card(self):
        self.click_element(HomePageLocators.FIRST_INGREDIENT_CARD)

    def is_ingredient_modal_visible(self):
        return self.check_element_visibility(HomePageLocators.INGREDIENT_DETAILS_POPUP_HEADER)

    def click_cross_button_for_ingredient_modal(self):
        self.click_element(HomePageLocators.INGREDIENT_DETAILS_POPUP_CROSS_BUTTON)
        self.wait_until_invisibility(HomePageLocators.INGREDIENT_DETAILS_POPUP_HEADER)

    def drag_first_ingredient_and_drop_to_basket(self):
        ingredient = self.find_element_with_wait(HomePageLocators.FIRST_INGREDIENT_CARD)
        basket = self.find_element_with_wait(HomePageLocators.BURGER_CONSTRUCTION_SECTION)
        self.drag_and_drop(ingredient, basket)

    def get_counter_value_for_first_ingredient(self):
        return self.get_text_from_element(HomePageLocators.FIRST_INGREDIENT_COUNTER)

    def click_create_order_button(self):
        self.click_element(HomePageLocators.CREATE_ORDER_BUTTON)

    def get_order_id(self):
        self.wait_until_invisibility(HomePageLocators.LOADER_ON_CREATE_ORDER_POPUP)
        return self.get_text_from_element(HomePageLocators.ORDER_ID)

    def click_cross_button_for_order(self):
        self.wait_until_invisibility(HomePageLocators.MODAL_OVERLAY)
        self.click_element(HomePageLocators.ORDER_POPUP_CROSS_BUTTON)
