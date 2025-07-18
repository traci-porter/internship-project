from behave import given, when, then

@given('Open the main page')
def open_main(context):
    context.driver.get('https://soft.reelly.io/sign-in')

@when('Log in to the page')
def log_in_steps(context):
    context.app.sign_in_page.log_in_steps()

@when('Click the Secondary option on the left side menu')
def click_secondary_option(context):
    context.app.secondary_option_page.click_secondary_option()

@then('Verify the correct page opens')
def verify_correct_page_opens(context):
    context.app.secondary_option_page.verify_correct_page_opens()

@then('Go to the final page using the pagination button')
def final_page(context):
    context.app.secondary_option_page.final_page()

@then('Go to the first page using the pagination button')
def last_page(context):
    context.app.secondary_option_page.first_page()
    context.app.secondary_option_page.verify_on_first_page()