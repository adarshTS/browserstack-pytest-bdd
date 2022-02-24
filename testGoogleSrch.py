import pytest
from selenium import webdriver
import sys
import os, json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pytest_bdd import scenario, given, when, then, parsers

from environment import start_local, stop_local

config_file_path = "config/single.json"
print("Path to the config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

# Edit these to match your credentials
USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or sys.argv[1]
BROWSERSTACK_ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY') or sys.argv[2]

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")


@scenario('features/googlesrch.feature', 'can find search results')
def test_googlesrch():
    pass


@pytest.fixture
def browser():
    url = "https://%s:%s@hub.browserstack.com/wd/hub" % (
        USERNAME, BROWSERSTACK_ACCESS_KEY
    )
    desired_capabilities = CONFIG['capabilities']
    for key in CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = CONFIG["capabilities"][key]

    print("Local=>"+desired_capabilities["browserstack.local"])
    if "browserstack.local" in desired_capabilities and desired_capabilities["browserstack.local"]:
        start_local()
    b = webdriver.Remote(command_executor=url, desired_capabilities=desired_capabilities)
    b.implicitly_wait(10)
    yield b
    b.quit()
    stop_local()


@given(parsers.parse('I visit url "{google}"'))
def navigate_search_url(browser, google):
    browser.get(google)
    sleep(5)


@when(parsers.parse('I search for "{text}"'))
def go_to_article(browser, text):
    if not "Google" in browser.title:
        raise Exception("Are you not on google? How come!")
    elem = browser.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.submit()
    browser.implicitly_wait(10)


@then(parsers.parse('title changes to "{title}"'))
def title_change(browser, title):
    print(browser.title)
    assert title == browser.title
