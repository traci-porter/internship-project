from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify Circle page has {number} or more cells')
def verify_circle_page_cells(context, number):
    print(type(number))
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components/CellsComponent/Link']")
    print(cells)

    assert len(cells) >= 10, f'Expected at least {number} cells but got {len(cells)}'
