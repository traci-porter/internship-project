from selenium.webdriver.common.by import  By
from time import sleep

from pages.base_page import  Page

class TargetAppPage(Page):
    TC_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")

    def open_target_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_conditions_link(self):
        print(f"Before click: {self.driver.window_handles}")
        self.click(*self.TC_LINK)
        sleep(2)  # Temp: allow time for the new window to spawn
        print(f"After click: {self.driver.window_handles}")