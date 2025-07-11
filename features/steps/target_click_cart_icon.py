from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open Target page')
#def open_target(context):
#    context.driver.get('https://www.target.com/')

#@when('Click on cart icon')
#def click_cart_icon(context):
#    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
#    sleep(5)

@then('Cart is empty')
def cart_is_empty(context):
    message_element = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    assert message_element.text == "Your cart is empty"
    sleep(10)