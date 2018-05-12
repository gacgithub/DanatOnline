from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hamcrest import assert_that, contains_string, equal_to
from selenium.common.exceptions import TimeoutException
from behave import *
import pdb
from features.lib.pages.home_page import HomePage
from helpers.utilities import Utilities

use_step_matcher("parse")


@given(u'I navigate to "{page}" page')
def step_given_I_navigate_to(context, page):
    context.driver.get(context.base_url)


@then(u'I verify the "{page}" page as "{user}" user')
def step_impl(context, page, user):
    home_page = HomePage()

    if page=='home' and user=='normal':
        Utilities.wait_for_element(context, home_page.LOGIN_BUTTON)
    elif page=='home' and user=='real':
        Utilities.wait_for_element(context, home_page.PROFILE_NAME)
    else:
        print('case not matched')


@when(u'I login as a real user')
def step_impl(context):
    home_page = HomePage()
    home_page.login(context)
