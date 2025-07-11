from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

VERIFY_SIGN_IN = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")


@when('Enter valid email address')
def enter_email_address(context):
    context.app.sign_in.enter_email_address()

@when('Click continue')
def click_continue(context):

    sleep(3)

@when('Click Create account with password')
def click_account_with_password(context):
    context.app.sign_in.click_account_with_password()

@when('Enter incorrect password')
def enter_incorrect_password(context):
    context.app.sign_in.enter_incorrect_password()


@when('Click sign in with incorrect password')
def click_sign_in(context):
    context.driver.find_element(By.ID, "login").click()
    sleep(5)

@then('Verify error message displays')
def sign_in_password(context):
    context.app.sign_in.sign_in_password()

@then('Verify Sign in form opens')
def verify_sign_in(context):
    context.app.sign_in.verify_sign_in()