from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Target product
@when('Input {word} into search field')
def input_search_word(context, word):
    search = context.driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']")
    search.clear()
    search.send_keys(word)
    sleep(2)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(1)

@then('Product results for {word} are shown')
def verify_results_text(context, word):
    expected_text = {word}
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text

    assert word.lower() in actual_text.lower(), f'Error, expected "{word}" not in actual "{actual_text}"'

