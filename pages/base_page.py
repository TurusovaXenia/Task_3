from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.base_url = base_url

    _DRAG_AND_DROP_SCRIPT = """
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

    def open(self, path=""):
        self.driver.get(f"{self.base_url}{path}")

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator)

    def check_element_visibility(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def fill_input(self, locator, text):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_attribute_in_element(self, locator, attribute, value):
        return self.wait.until(
            lambda d: value in d.find_element(*locator).get_attribute(attribute),
            message=f"Элемент {locator} не получил атрибут {attribute}='{value}'"
        )

    def drag_and_drop(self, source_element, target_element):
        self.driver.execute_script(self._DRAG_AND_DROP_SCRIPT, source_element, target_element)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
