from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hamcrest import assert_that, contains_string, equal_to
from selenium.common.exceptions import TimeoutException
from behave import *
# from features.lib.pages import PageFactory

use_step_matcher("re")

"""
This file contains steps from login page.
"""

@given(u'I navigate to (?P<page_name>.+) page')
def step_impl(context, page_name):
    context.driver.get("https://google.com/")
    # context.page = PageFactory(page_name)(context.driver)
    try:
        context.driver.get("https://www.argaam.com/en")
        # context.driver.get(context.base_url)
    except TimeoutException:
        print("page load time exceeded")

@then(u'I verify the home page as "bob" user')
def step_impl(context):
    context.driver.find_element_by_id("asdasd")
    # assert_that(context.browser.url.lower(), contains_string(context.page.PATH))



@when(u'I login as a real user')
def step_impl(context):
    context.driver.find_element_by_id("asdasd")


@then(u'I verify the home page as "real" user')
def step_impl(context):
    context.driver.find_element_by_id("asdasd")
    # raise NotImplementedError(u'STEP: Then I verify the home page as "real" user')
