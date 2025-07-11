from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome()

    ### SAFARI ###
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #context.driver = webdriver.Chrome(
    # options=options
     #)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #bs_user ='traciporter_cm2f0g'
    #bs_key = 'exVjc2Z8v5MpDFuQidp7'
    #url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'


    #bstack_options = {
     #"os" : "Windows",
     #"osVersion" : "11",
     #'browserName': 'Edge',
     #'sessionName': scenario_name,
     #"buildName": "Target Automation Build"
     #}

    #options = Options()
    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
