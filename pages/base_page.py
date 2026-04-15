from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.base_url = base_url

    def open(self, path=""):
        self.driver.get(f"{self.base_url}{path}")

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_existing_element(self, element):
        self.wait.until(EC.element_to_be_clickable(element)).click()

    def click_with_offset(self, locator):
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def type_text(self, locator, text):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def drag_and_drop(self, source_element, target_element):
        script = """
        var source = arguments[0];
        var target = arguments[1];
        var dataTransfer = new DataTransfer();

        var dragStartEvent = new DragEvent('dragstart', { dataTransfer: dataTransfer, bubbles: true });
        source.dispatchEvent(dragStartEvent);

        var dropEvent = new DragEvent('drop', { dataTransfer: dataTransfer, bubbles: true });
        target.dispatchEvent(dropEvent);

        var dragEndEvent = new DragEvent('dragend', { dataTransfer: dataTransfer, bubbles: true });
        source.dispatchEvent(dragEndEvent);
        """
        self.driver.execute_script(script, source_element, target_element)

    def get_element_from_list_by_text(self, items_locator, target_text):
        elements = self.find_elements_with_wait(items_locator)
        for el in elements:
            if target_text in el.text:
                return el
        raise Exception(f"Элемент с текстом {target_text} не найден в списке")

    def wait_for_attribute(self, locator, attribute, value):
        return self.wait.until(
            lambda d: value in d.find_element(*locator).get_attribute(attribute)
        )

    def wait_for_valid_text(self, locator, invalid_text):
        return self.wait.until(
            lambda d: self.get_text(locator).isdigit() and self.get_text(locator) != invalid_text
        )

    def wait_for_text_in_list(self, items_locator, text):
        def find_text_logic(_):
            for el in self.find_elements_with_wait(items_locator):
                if text in el.text:
                    return True
            return False

        try:
            return self.wait.until(find_text_logic)
        except TimeoutException:
            return False
