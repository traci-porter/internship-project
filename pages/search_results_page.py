from selenium.webdriver.common.by import By
#from features.steps.search_results_page_steps import SEARCH_RESULTS_TXT
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
#from time import sleep

class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    SEARCH_CART = (By.XPATH, "//h1[text()='Your cart is empty']")
    FAV_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TT_TEXT = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    def verify_search_results(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"

    def cart_is_empty(self):
        message_element = self.find_element(*self.SEARCH_CART).text
        assert message_element.text == "Your cart is empty"

    def hover_fav_icon(self):
        self.hover_element(*self.FAV_ICON)

    def verify_fav_tt_shown(self):
        self.wait_for_element(self.FAV_TT_TEXT)
