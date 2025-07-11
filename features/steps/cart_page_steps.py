from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click Target product A-92785491 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/tazo-tea/-/A-92785491?preselect=16227390#lnk=sametab')

@when('Click the add to cart button')
def click_cart_button(context):
    context.app.cart_page.click_cart_button()
    sleep(3)

@when("Click 'View cart & check out' button")
def click_checkout_button(context):
    context.app.cart_page.click_checkout_button()

@then('Verify product is in cart')
def verify_product_in_cart(context):
    context.app.cart_page.verify_product_in_cart()

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()



