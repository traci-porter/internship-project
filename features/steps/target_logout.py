from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CLICK_ACCOUNT = (By.XPATH, "//a[@id='account-sign-in']")
SIGN_IN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
OPENED_SIGN_IN_FORM = (By.XPATH, "//h1[text()='Sign in or create account']")


@when('Click on Account')
def click_account_icon(context):
    context.driver.find_element(*CLICK_ACCOUNT).click()
    sleep(2)

@when('Click on sign in')
def click_sign_in_icon(context):
    context.driver.find_element(*SIGN_IN).click()
    sleep(2)

@then('Open sign in form')
def open_sign_in_form(context):
    message_element = context.driver.find_element(*OPENED_SIGN_IN_FORM)
    assert message_element.text == "Sign in or create account"
    print('Test case passed')




