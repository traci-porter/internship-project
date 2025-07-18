from features.steps.header_steps import SEARCH_FIELD, CART_ICON
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import ElementClickInterceptedException


class ReellySecondaryPage(Page):
    def click_secondary_option(self):
        wait = WebDriverWait(self.driver, 20)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/secondary-listings']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

        # Wait for navigation to complete
        wait.until(EC.url_contains("/secondary-listings"))
        print("✅ Clicked on Secondary Listings and navigated")

    def verify_correct_page_opens(self):
        actual_page = self.driver.current_url
        print(f"Actual page URL: {actual_page}")
        expected_page = "https://soft.reelly.io/secondary-listings"
        assert actual_page == expected_page, f"Expected URL '{expected_page}', but got '{actual_page}'"

    def wait_for_page_to_update(self, wait, expected_page):
        def check_page(driver):
            elem = driver.find_element(By.XPATH, "//div[@wized='currentPageProperties']")
            text = elem.text.strip()
            print(f"🔍 Found text: '{text}', expecting page {expected_page}")
            if text == '':
                return False
            try:
                return int(text) == expected_page
            except ValueError:
                return False

        try:
            wait.until(check_page)
            print(f"✅ Page updated to {expected_page}")
        except TimeoutException:
            raise Exception(f"❌ Timeout: Page did not update to {expected_page}")

    def first_page(self):
        wait = WebDriverWait(self.driver, 15)

        def get_current_page():
            try:
                element = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@wized='currentPageProperties']"))
                )
                text = element.text.strip()
                print(f"Current page text: '{text}'")
                return int(text) if text.isdigit() else None
            except Exception as e:
                print(f"⚠️ Error reading current page: {e}")
                return None

        while True:
            current_page = None

            # Try to get current page number up to 10 times, waiting 1 second between tries
            for _ in range(5):
                current_page = get_current_page()
                if current_page is not None:
                    break
                time.sleep(1)
            if current_page is None:
                raise Exception("❌ Could not read current page number.")

            if current_page <= 1:
                print("✅ Reached the first page.")
                break

            try:
                prev_button_xpath = "//*[@wized='previousPageButton' or @wized='previousPageMLS']"
                prev_button = wait.until(EC.element_to_be_clickable((By.XPATH, prev_button_xpath)))
                print("🔘 Previous button found and clickable. Clicking...")

                try:
                    prev_button.click()
                except ElementClickInterceptedException:
                    print("⚠️ Regular click failed, trying JavaScript click...")
                    self.driver.execute_script("arguments[0].click();", prev_button)

                # Wait for page number to decrease
                wait.until(lambda d: (cp := get_current_page()) is not None and cp < current_page)

            except TimeoutException:
                print("❌ Previous button not clickable or page did not update.")
                raise

    def verify_on_first_page(self):
        current_page_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@wized='currentPageProperties']"))
        )
        current_page = int(current_page_element.text.strip())
        assert current_page == 1, f"Expected page 1, but was on page {current_page}"
        print("✅ Verified: You are on page 1.")

    def final_page(self):
        wait = WebDriverWait(self.driver, 10)

        while True:
            current_page_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@wized='currentPageProperties']"))
            )
            current_page_text = current_page_element.text.strip()
            if not current_page_text:
                continue
            current_page = int(current_page_text)

            total_pages_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@wized='totalPageProperties']"))
            )
            total_pages = int(total_pages_element.text.strip())

            if current_page >= total_pages:
                print(f"Reached the last page: {current_page}")
                break

            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@wized='nextPageMLS']"))
            )
            next_button.click()

            try:
                self.wait_for_page_to_update(wait, current_page + 1)
            except Exception as e:
                print(f"⚠️ Warning: {e}")
                # Optionally break or continue, depending on your tolerance for failures
                break



