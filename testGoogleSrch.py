import pytest
from selenium import webdriver
import sys
import os, json
from time import sleep
from pytest_bdd import scenario, given, when, then, parsers


config_file_path = "config/single.json"
print("Path to the config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or sys.argv[1]
BROWSERSTACK_ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY') or sys.argv[2]

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")


@scenario('features/googlesrch.feature', 'can find search results')
def test_googlesrch():
    pass


browser = webdriver.Remote(
    command_executor="https://hub-cloud.browserstack.com/wd/hub"
)

@given(parsers.parse('I visit url "{google}"'))
def navigate_search_url(google):
    browser.get(google)
    sleep(5)


@when(parsers.parse('I search for "{text}"'))
def go_to_article(text):
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
