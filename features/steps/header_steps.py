from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test* = '@web/GlobalHeader/UtilityHeader/']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/Product']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

@when('Search for {search_word}')
def search_product(context, search_word):
    #context.driver.find_element(By.ID, 'search').send_keys(search_word)
    #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #sleep(5)
    context.app.header.search_product()

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()

@when('Click Sign In from side nav menu')
def click_side_nav(context):
    context.app.header.click_side_nav()

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'
