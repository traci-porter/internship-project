from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TermsConditionsPage(Page):
    def verify_tc_opened(self):
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        self.wait_for_url_contains('terms-conditions')