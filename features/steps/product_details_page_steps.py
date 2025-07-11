from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, ".styles_headerWrapper__Xzdtg")

@given('Open target product A-94299326 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/women-s-short-sleeve-button-down-t-shirt-universal-thread/-/A-94299326?preselect=94264668#lnk=sametab')
    sleep(4)

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Heather Gray', 'Olive Green', 'Pink']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS) #[webelement1, webelement2, webelement3, webelement4]
    print(colors)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

