from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    #def click(self, *locator):
    #    self.driver.find_element(*locator).click()

    def click(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception as e:
            print(f"Click intercepted: {e}, trying JS click")
            self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url))

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def get_current_window_id(self):
        window = self.driver.current_window_handle
        print(f'Original window: {window}')
        return window

    def switch_to_new_window(self, old_handles):
        self.wait.until(lambda d: len(d.window_handles) > len(old_handles))
        new_window = [w for w in self.driver.window_handles if w not in old_handles][0]
        print(f"Switching to new window: {new_window}")
        self.driver.switch_to.window(new_window)

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to window: {window_id}')
        self.driver.switch_to.window(window_id)

    def close_window(self):
        self.driver.close()

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text