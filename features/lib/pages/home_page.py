from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from helpers.utilities import Utilities
# import features.lib.locators.home_locators as locators

class HomePage:

    LOGIN_BUTTON = (By.CSS_SELECTOR, '[onclick="ShowLoginPopup();"]')
    PROFILE_NAME = (By.CSS_SELECTOR, '[id="profileDisplayName"]')
    USERNAME_FIELD = (By.CSS_SELECTOR, '[id="UserName"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[id="pass"]')
    SUBMIT_LOGIN = (By.CSS_SELECTOR, '[id="btnSubmit"]')

    def login(self, context):
        Utilities.click_element(context, self.LOGIN_BUTTON)
        Utilities.input_text(context, self.USERNAME_FIELD, 'sams.prashanth@gmail.com')
        Utilities.input_text(context, self.PASSWORD_FIELD, '75124fcf')
        Utilities.click_element(context, self.SUBMIT_LOGIN)
