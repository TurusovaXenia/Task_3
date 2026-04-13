from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class*=button]")
    MODAL_OVERLAY = (By.XPATH, "(.//div[contains(@class, 'Modal_modal_overlay')])[2]")
    BURGER_CONSTRUCTION_SECTION = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket']")
    FIRST_INGREDIENT_CARD = (By.XPATH, "(.//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH,
                                "(.//a[contains(@class, 'BurgerIngredient_ingredient')])[1]//p[contains(@class, 'counter')]")
    INGREDIENT_DETAILS_POPUP_HEADER = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    INGREDIENT_DETAILS_POPUP_CROSS_BUTTON = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'] button")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    LOADER_ON_CREATE_ORDER_POPUP = (By.CSS_SELECTOR,
                                    "div[class*='Modal_modal_opened'] img[class*='Modal_modal__loading']")
    ORDER_ID = (By.CSS_SELECTOR, "h2[class*='Modal_modal']")
    ORDER_POPUP_CROSS_BUTTON = (By.CSS_SELECTOR, "button[class*='button']")
