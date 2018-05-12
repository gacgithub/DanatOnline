from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb

class Utilities:

    def wait_for_element(context, locator):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.presence_of_element_located((locator)))

    def wait_for_visible(context, locator):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.visibility_of_element_located((locator)))

    def wait_for_clickable(context, locator):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.element_to_be_clickable((locator)))

    def click_element(context, locator):
        Utilities.wait_for_element(context, locator)
        Utilities.wait_for_visible(context, locator)
        Utilities.wait_for_clickable(context, locator)
        context.driver.find_element(locator[0], locator[1]).click()

    def input_text(context, locator, text):
        Utilities.wait_for_element(context, locator)
        Utilities.wait_for_visible(context, locator)
        context.driver.find_element(locator[0], locator[1]).send_keys(text)
