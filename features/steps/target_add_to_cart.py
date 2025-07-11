from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

#Locators
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
PRODUCT_OPTIONS = (By.XPATH,
     "//button[@data-test='orderPickupButton' and @id='addToCartButtonOrTextIdFor90296387']")
VIEW_CART = (By.XPATH, "//a[contains(text(), 'View cart')]")
VERIFY_PRODUCT = (By.XPATH, "//div[@data-test='cartItem-title']")

#def safe_click(driver, by, locator, timeout=10):
    #element = WebDriverWait(driver, timeout).until(
    #    EC.element_to_be_clickable((by, locator))
    #)
    #driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    #driver.execute_script("arguments[0].click();", element)

#@when('Click the add to cart button')
#def click_add_cart(context):
#    context.driver.find_element(*PRODUCT_NAME).click()
#    #   sleep(3)

@when('Choose options and add to cart')
def choose_options(context):
    context.driver.find_element(*PRODUCT_OPTIONS).click()
   # sleep(3)

@when('Click view cart')
def click_view_cart(context):
    print("Running 'Click view cart' step")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(VIEW_CART)
    ).click()
    # sleep(3)

@then("Verify 'V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans' is in the cart")
def verify_product_in_cart(context):
    actual_product = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(VERIFY_PRODUCT)
    ).text

    expected = "V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans".lower().strip()
    actual = actual_product.lower().strip()
    assert expected in actual, f'Expected product "{expected}" not found in cart. Found "{actual_product}" instead.'

#@then("Verify product is in cart")
#def verify_product_in_cart(context):
#    actual_product = WebDriverWait(context.driver, 10).until(
#        EC.visibility_of_element_located(VERIFY_PRODUCT)
#    ).text
#    expected = 'Tazo Tea'
#    actual_product = actual_product.lower().strip()
#    assert expected in actual_product, f'Expected product "{expected}" not found in cart. Found "{actual_product}" instead.'