from behave import given, when, then
from selenium import webdriver

from features.steps.pages import *


@given('a user visit google')
def step_impl(context):
    context.driver = webdriver.Chrome("C:/drivers/chromedriver.exe")
    page = SearchPage(context)
    page.load('http://www.google.com')


@when('the user searches for the behave python phrase')
def step_impl(context):
    page = SearchPage(context)
    page.search('behave python')


@then('one of the results contains: Welcome to behave')
def step_impl(context):
    page = ResultPage(context)
    results = page.phrase_result_count('Welcome to behave')
    context.driver.quit()
    assert results > 0