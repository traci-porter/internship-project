from features.steps.header_steps import SEARCH_FIELD, CART_ICON
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

def wait_for_overlay_to_disappear(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)
    try:
        overlay = driver.find_element(By.ID, "weglot-listbox")
        if overlay.is_displayed():
            wait.until(EC.invisibility_of_element_located((By.ID, "weglot-listbox")))
    except NoSuchElementException:
        pass
    except TimeoutException:
        print("Warning: Overlay 'weglot-listbox' did not disappear within timeout")

class ReellySecondaryPage(Page):

    def hide_weglot_overlay(self):
        try:
            self.driver.execute_script("""
                const overlay = document.getElementById('weglot-listbox');
                if (overlay && overlay.style.display !== 'none') {
                    overlay.style.display = 'none';
                    console.log('✅ Weglot overlay hidden');
                }
            """)
        except Exception as e:
            print(f"⚠️ Failed to hide Weglot overlay: {e}")

    def click_secondary_option(self):
        wait = WebDriverWait(self.driver, 20)

        # Optional: Hide Weglot overlay
        self.hide_weglot_overlay()

        # Click Off-plan button
        off_plan = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.menu-link.w-inline-block[wized='newOffPlanLink']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", off_plan)
        self.driver.execute_script("arguments[0].click();", off_plan)

        secondary = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Secondary']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", secondary)
        self.driver.execute_script("arguments[0].click();", secondary)

        # Confirm the page has loaded
        wait.until(EC.url_contains("/secondary-listings"))
        print("✅ Navigated directly to Secondary Listings")

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
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[wized='currentPageProperties']")))
                elem = self.driver.find_element(By.CSS_SELECTOR, "div[wized='currentPageProperties']")
                page_text = elem.text.strip()
                return int(page_text)
            except Exception as e:
                print(f"⚠️ Failed to read current page number: {e}")
                return None

        previous_button_locator = (By.CSS_SELECTOR, "div[wized='previousPageMLS']")

        current_page = get_current_page()
        if current_page is None:
            raise Exception("❌ Could not read the current page number.")

        print(f"🔢 Starting at page {current_page}")

        while current_page and current_page > 1:
            try:
                prev_button = wait.until(EC.element_to_be_clickable(previous_button_locator))
                print("🔘 Previous button found and clickable. Clicking...")

                try:
                    prev_button.click()
                except Exception:
                    print("⚠️ Regular click failed, trying JavaScript click...")
                    self.driver.execute_script("arguments[0].click();", prev_button)

                # Wait for page to update to a lower page number
                wait.until(lambda d: (cp := get_current_page()) is not None and cp < current_page)
                current_page = get_current_page()
                print(f"📄 Current page text: '{current_page}'")

            except Exception as e:
                print(f"❌ Previous button not clickable or page did not update: {e}")
                break

    def verify_on_first_page(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[wized='currentPageProperties']")))

        # Wait until the element's text is not empty
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR,"div[wized='currentPageProperties']").text.strip() != '')

        current_page_element = self.driver.find_element(By.CSS_SELECTOR, "div[wized='currentPageProperties']")
        current_page = int(current_page_element.text.strip())

        print(f"✅ Current page is: {current_page}")
        assert current_page == 1, f"Expected to be on first page (1), but on page {current_page}"

    ## FOR LOCAL SETUP
    # def final_page(self):
    #     wait = WebDriverWait(self.driver, 10)
    #
    #     while True:
    #         current_page_element = wait.until(
    #             EC.presence_of_element_located((By.XPATH, "//div[@wized='currentPageProperties']"))
    #         )
    #         current_page_text = current_page_element.text.strip()
    #         if not current_page_text:
    #             continue
    #         current_page = int(current_page_text)
    #
    #         total_pages_element = wait.until(
    #             EC.presence_of_element_located((By.XPATH, "//div[@wized='totalPageProperties']"))
    #         )
    #         total_pages = int(total_pages_element.text.strip())
    #
    #         if current_page >= total_pages:
    #             print(f"Reached the last page: {current_page}")
    #             break
    #
    #         next_button = wait.until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, "a[wized='nextPageMLS']"))
    #         )
    #         # Scroll into view
    #         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
    #         # Click with JS to avoid intercept
    #         self.driver.execute_script("arguments[0].click();", next_button)
    #
    #         print("✅ Clicked the pagination next button using JS")
    #
    #         try:
    #             self.wait_for_page_to_update(wait, current_page + 1)
    #         except Exception as e:
    #             print(f"⚠️ Warning: {e}")
    #             # Optionally break or continue, depending on your tolerance for failures
    #             break


    #FOR BROWSERSTACK TO MINIMIZE TIME
    def final_page(self):
        wait = WebDriverWait(self.driver, 10)

        for page in range(0, 3):
            sleep(5)
            next_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[wized='nextPageMLS']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
            self.driver.execute_script("arguments[0].click();", next_button)


