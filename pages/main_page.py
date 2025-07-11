from pages.base_page import Page

class MainPage(Page):
    def open_main_page(self):
        self.driver.get('https://www.target.com/')

    def open_product_page(self):
        self.driver.get('https://www.target.com/p/tazo-tea/-/A-92785491?preselect=16227390#lnk=sametab')
