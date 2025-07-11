from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from features.steps.header_steps import SEARCH_FIELD, CART_ICON
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_MSG = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/cart']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

    def click_cart_button(self):
        self.click(*self.ADD_TO_CART)
        sleep(5)
        #element = WebDriverWait(self.driver, 10).until(
        #    EC.visibility_of_element_located(self.ADD_TO_CART)
        #)
        ##self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        #element.click()

    def wait_for_overlay_to_disappear(self, timeout=10):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay, .spinner, .modal"))
            )
        except TimeoutException:
            pass

    def click_checkout_button(self):
        # Wait for overlays to disappear before trying to click
        self.wait_for_overlay_to_disappear()

        # Wait for the checkout button to be clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_CHECKOUT_BUTTON)
        )

        # Scroll it into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Try clicking normally
        try:
            element.click()
        except Exception as e:
            print(f"Click intercepted or failed: {e}. Using JS click fallback.")
            self.driver.execute_script("arguments[0].click();", element)

    def verify_product_in_cart(self):
        self.wait_for_overlay_to_disappear()

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_MSG)
        )

        actual_text = element.text.strip().lower()
        expected_text = 'tazo skinny latte chai black tea concentrate'

        assert expected_text in actual_text, (
            f"Error: Expected product '{expected_text}' not found in cart.\n"
            f"Actual text found: '{actual_text}'"
        )

    def verify_cart_empty(self):
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        expected_test = 'Your cart is empty'
        assert actual_text == expected_test, f"Error, expected {expected_test} but got actual {actual_text}"