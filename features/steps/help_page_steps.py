from behave import given, when, then


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic Gift Cards')
def select_giftcards(context):
    context.app.help_page.select_giftcards()


#@then('Verify help {expected_header_text} page opened')
#def verify_help_page_opened(context, expected_header_text):
#    context.app.help_page.verify_help_page_opened(expected_header_text)


@then('Verify help Returns page opened')
def verify_returns_opened(context):
    context.app.help_page.verify_returns_opened()


@then('Verify help Target GiftCard balance page opened')
def verify_giftcards_opened(context):
    context.app.help_page.verify_giftcards_opened()