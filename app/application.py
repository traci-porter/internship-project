from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.terms_conditions_page import TermsConditionsPage
from pages.sign_in_page import SignInPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)
        self.sign_in = SignInPage(driver)

#app = Application()
#app.main_page.open_main_page()
#app.header.search_product()
