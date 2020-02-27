from behave import given, when, then


@given('a user visit google')
def step_impl(context):
    context.web.open('http://www.google.com')


@when('the user searches for the behave python phrase')
def step_impl(context):
    search_input = context.web.find_by_xpath("//input[@name='q']")
    search_input.send_keys("behave python")


@then('one of the results contains: Welcome to behave')
def step_impl(context):
    xpath = "//*[contains(text(), 'Welcome to behave')]"
    results = context.web.finds_by_xpath(xpath)
    assert len(results) > 0
