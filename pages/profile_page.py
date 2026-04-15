import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Проверка отображения уникального элемента страницы 'Профиль'")
    def is_profile_form_visible(self):
        self.wait_until_visible(ProfilePageLocators.PROFILE_FORM)
        return self.is_element_visible(ProfilePageLocators.PROFILE_FORM)

    @allure.step("Клик на кнопку 'История заказов'")
    def click_order_history_button(self):
        self.click_with_offset(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Клик на кнопку 'Выход'")
    def click_logout_button(self):
        self.click_with_offset(ProfilePageLocators.LOGOUT_BUTTON)
