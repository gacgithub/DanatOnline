import os
import time
import logging
import data
from selenium import webdriver
from behave.log_capture import capture


RUNTIME_DIR = os.path.join(
    os.path.abspath(
        os.path.join(
            __file__, os.pardir, os.pardir,
            'screenshot', time.strftime('%d.%m.%Y - %R')
        )
    )
)


def before_all(context):
    print("Executing before all")
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(50)
    context.driver.set_page_load_timeout(50)

    # context.base_url = data.url


def after_all(context):
    context.driver.quit()


@capture
def after_step(context, step):
    if step.status == "failed":
        make_dir(RUNTIME_DIR)
        screenshot = os.path.join(
            RUNTIME_DIR, context.scenario.name + " - " + step.name + '.png')
        context.driver.save_screenshot(screenshot)
        logging.error("Screenshot saved to file: %s" % screenshot)


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

# def after_scenario(context):

# def after_feature(context, feature):
#     context.driver.close()
