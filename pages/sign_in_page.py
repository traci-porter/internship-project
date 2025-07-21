from features.steps.header_steps import SEARCH_FIELD, CART_ICON
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SignInPage(Page):
    VERIFY_SIGN_IN = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")

    def verify_sign_in(self):
        actual_text = self.find_element(*self.VERIFY_SIGN_IN).text
        expected_text = 'Sign in or create account'
        assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"

    def click_continue(self):
        self.driver.find_element(By.ID, "login").click()

    def enter_email_address(self):
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        email_input.send_keys("traci707@gmail.com")  # Replace with real test email
        continue_btn = self.driver.find_element(By.ID, "login")
        continue_btn.click()

    def click_account_with_password(self):
        self.driver.find_element(By.ID, "password-checkbox").click()

    def enter_incorrect_password(self):
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("WrongPassword123")

    def sign_in_password(self):
        sign_in_btn = self.driver.find_element(By.ID, "password")
        sign_in_btn.click()

    def verify_error_message(self):
        error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='authErrorMessage']")))
        self.assertIn("incorrect", error.text.lower())

    def log_in_steps(self):
        print("⏳ Trying to log in...")
        print("Current URL:", self.driver.current_url)
        self.driver.save_screenshot("login_page_debug.png")

        self.driver.get("https://soft.reelly.io/sign-in")
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//form")))

        wait.until(EC.presence_of_element_located((By.ID, "email-2"))).send_keys("traci707@gmail.com")
        wait.until(EC.presence_of_element_located((By.ID, "field"))).send_keys("Password1")

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[wized='loginButton']")))
        login_button.click()

        # Wait until dashboard or menu is visible
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/secondary-listings')]")))
        print("✅ Logged in successfully")


