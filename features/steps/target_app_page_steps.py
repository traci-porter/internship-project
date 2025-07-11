from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open sign in page')
def open_target_sign_in_page(context):
    context.app.target_app_page.open_target_sign_in_page()

@when('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()

@when('Click on Target terms and conditions link')
def click_terms_conditions_link(context):
    context.old_windows = context.driver.window_handles  # 🟢 Capture BEFORE click
    context.app.target_app_page.click_terms_conditions_link()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window(context.old_windows)

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()


@then('User can close new window and switch back to original')
def close_window(context):
    context.app.base_page.close_window()
