from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import *

class HomeLocators:

    USERNAME_FIELD = (By.CSS_SELECTOR, '')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '')

    def __init__(self):
        super(HomeLocators, self).__init__()