from features.steps.header_steps import SEARCH_FIELD, CART_ICON
from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ACCOUNT_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    EMAIL_FIELD = (By.ID, 'username')
    CONTINUE_BTN = (By.ID, 'login')


    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.ACCOUNT_BTN)

    def click_side_nav(self):
        self.click(*self.SIGN_IN)
        #self.input_text('traciporter@hotmail.com','*self.EMAIL_FIELD)